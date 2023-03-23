coffee_machine_on = True

global resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

global resources_left
resources_left = {"water": 0, "milk": 0, "coffee": 0, "money": 0}


def coffee_machine():
    menu = {
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

    # Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    # This input also takes two hidden inputs: "Off" ends the program and "Report" which prints the current resources

    user_input = (input("What would you like? (espresso/latte/cappuccino):").lower())

    def resource_check(order):
        enough_resources = []
        for ingredient in menu[order]["ingredients"]:
            drink_ingredient = (menu[order]["ingredients"][ingredient])
            global resources
            resources_ingredient = resources[ingredient]
            if resources_ingredient < drink_ingredient:
                print(f"Sorry there is not enough {ingredient} to make your {user_input}")
                enough_resources.append("no")
            else:
                global resources_left
                resources_left[ingredient] = resources_ingredient - drink_ingredient
        return enough_resources.count("no"), resources_left

    # if user enters a coffee drink (espresso, latte, cappuccino)
    if user_input in menu.keys():
        make_drink, updated_resources = resource_check(user_input)
        # Value of make_drink is zero if there are sufficient ingredients
        if make_drink == 0:
            global resources
            resources = updated_resources
            wallet = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
            cost = menu[user_input]['cost']
            print(f"The cost for a {user_input} is ${cost}0. Please insert coins:")
            for coins in wallet:
                wallet.update({coins: int(input(f"How many {coins}?"))})

            total = (wallet["quarters"] * 0.25) + (wallet["dimes"] * 0.10) + (wallet["nickels"] * 0.05) + (
                        wallet["pennies"] * 0.01)

            if total >= cost:
                print(f"Here's your {user_input}.  Your change is ${round(total - cost, 2)}")
                resources["money"] = resources["money"] + cost
            else:
                print(f"Sorry ${total}0 is insufficient.  Refunding ${total}0")
    elif user_input == "report":
        for ingredient in resources:
            print(f"{ingredient}:{resources[ingredient]}")
    else:
        global coffee_machine_on
        coffee_machine_on = False


while coffee_machine_on:
    coffee_machine()

