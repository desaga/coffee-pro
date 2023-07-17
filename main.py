"""
CoffeePro The Coffee Machine Program.
Basic functions:
- makes 3 types of drink
- process coins
- refill resources
- print a report (money, resources)
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

CHOICES = [
    "espresso",
    "latte",
    "cappuccino",
    "off",
    "report",
    "service"
]

resources = {}


def get_choice():
    while True:
        response = input("What would you like? (espresso/latte/cappuccino): >")
        if response in CHOICES:
            return response
        else:
            print(f"Oops! It seems like there was a mistake in your input \"{response}\". Could you please try again?")


def make_drink(drink_type):
    """Makes a drink"""
    drink = MENU[drink_type]
    # use resources
    for item in MENU[drink_type]["ingredients"]:
        resources[item]["amount"] -= MENU[drink_type]["ingredients"][item]
    print(f"Here is your {drink_type}. Enjoy.")
    return True


def process_coins(drink_type):
    """Collects money, gives change, adds money to cash register. Returns True if transaction successful or
    refund/cancel"""
    total_paid = 0
    drink_cost = MENU[drink_type]["cost"]
    print(f"Your {drink_type} costs ${drink_cost} Please insert coins")
    total_paid += int(input("How many quarters ($0.25)? >")) * 0.25
    if drink_cost - total_paid > 0:
        print(f"You paid ${total_paid:.2f}. Remaining amount is ${drink_cost - total_paid:.2f}")
        total_paid += int(input("How many dimes ($0.10)? >")) * 0.10
    if drink_cost - total_paid > 0:
        print(f"You paid ${total_paid:.2f}. Remaining amount is ${drink_cost - total_paid:.2f}")
        total_paid += int(input("How many nickels ($0.05)? >")) * 0.05
    if drink_cost - total_paid > 0:
        print(f"You paid ${total_paid:.2f}. Remaining amount is ${drink_cost - total_paid:.2f}")
        total_paid += int(input("How many pennies ($0.01)? >")) * 0.01
    if total_paid - drink_cost >= 0:
        if total_paid - drink_cost > 0:
            print(f"Here is ${total_paid - drink_cost:.2f} dollars in change.")
        resources["money"]["amount"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources(drink_type):
    """Returns True if enough resources"""
    for item in MENU[drink_type]["ingredients"]:
        print(MENU[drink_type]["ingredients"][item])
        if resources[item]['amount'] < MENU[drink_type]["ingredients"][item]:
            print(f"Sorry there is not enough {item}. Service required.")
            return False
    return True


def print_report():
    """Prints amount of resources"""
    print("Coffee machine resources report")
    for item in resources:
        if item == "money":
            print(f"{item} \t{resources[item]['unit']}{resources[item]['amount']}")
        else:
            print(f"{item} \t{resources[item]['amount']}{resources[item]['unit']}")


def restore_resources():
    """Restores resources, takes money from a cache storage"""
    global resources
    resources = {
        "water": {"amount": 300, "unit": "ml"},
        "milk": {"amount": 200, "unit": "ml"},
        "coffee": {"amount": 100, "unit": "g"},
        "money": {"amount": 0, "unit": "$"},
    }


# initializing and running the coffee machine
restore_resources()
turned_on = True
while turned_on:
    choice = get_choice()
    if choice == CHOICES[0] or choice == CHOICES[1] or choice == CHOICES[2]:  # make a drink
        if check_resources(choice) and process_coins(choice):
            make_drink(choice)
    elif choice == CHOICES[3]:  # turn off
        turned_on = False
    elif choice == CHOICES[4]:  # print report
        print_report()
    elif choice == CHOICES[5]:  # refill resources
        restore_resources()
    else:
        print("Error")
