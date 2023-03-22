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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# This input also takes two hidden inputs: "Off" Which ends the program and "Report" which prints the current resources
user_input = (input("What would you like? (espresso/latte/cappuccino):").lower())


def resource_check(order):
    enough_resources = []
    resources_left = {"water":[], "milk":[], "coffee":[]}
    for ingredient in MENU[order]["ingredients"]:
        drink_ingredient = (MENU[order]["ingredients"][ingredient])
        resources_ingredient = resources[ingredient]
        if resources_ingredient < drink_ingredient:
            print(f"Sorry there is not enough {ingredient} to make your {user_input}")
            enough_resources.append("no")
        else:
            resources_left[ingredient].append(resources_ingredient-drink_ingredient)
    return enough_resources.count("no"), resources_left


# if user enters a coffee drink (espresso, latte, cappuccino)
if user_input in MENU.keys():
    make_drink, updated_resources = resource_check(user_input)
    if make_drink == 0: # This value is zero if there are sufficient ingredients
        resources = updated_resources







