MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_machine():
    # TODO 1 Print Report
    def report():
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"money: ${profit}")
        coffee_machine()

    # TODO 2 CHeck resources sufficient
    def resources_sufficient(value):
        if MENU[value]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water.")
            coffee_machine()
        elif MENU[value]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk.")
            coffee_machine()
        elif MENU[value]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee.")
            coffee_machine()

    # TODO 3 process coins
    def process_coins():
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = ((quarters * 25) / 100) + ((dimes * 10) / 100) + ((nickels * 5) / 100) + ((pennies * 1) / 100)
        return total

    # TODO 4 check transaction successful
    def transaction_successful(amount):
        global profit
        cost = MENU[intake]["cost"]
        if amount > cost or amount > cost:
            change = amount - cost
            print(f"Here is ${round(change, 2)} in change.")
            profit += cost
        else:
            print("Sorry that's not enough money. Money refunded. ")
            coffee_machine()


    # TODO 5 Make coffee
    def make_coffee(coffee):
        ingre = MENU[coffee]["ingredients"]
        for item in resources and ingre:
            resources[item] = resources[item] - ingre[item]
        print(f"Here is your {coffee} ☕ Enjoy!")

    intake = input("What would you like? (espresso/latte/cappuccino): ")
    if intake == "report":
        report()
    elif intake == "off":
        print("Turning off!")
    elif intake == 'espresso' or intake == 'latte' or intake == 'cappuccino':
        resources_sufficient(intake)
        coin = process_coins()
        transaction_successful(coin)
        make_coffee(intake)
        coffee_machine()
    else:
        print("Invalid Input!")
        coffee_machine()


coffee_machine()
