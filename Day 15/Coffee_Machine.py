MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}


def check_resources(item):
    water_needed = MENU[item]["ingredients"]["water"]
    milk_needed = MENU[item]["ingredients"]["milk"]
    coffee_needed = MENU[item]["ingredients"]["coffee"]
    item_needed = ""
    if resources["water"] < water_needed:
        item_needed += " water"
    if resources["milk"] < milk_needed:
        item_needed += " milk"
    if resources["coffee"] < coffee_needed:
        item_needed += " coffee"
    if item_needed != "":
        print(f"Sorry there is not enough{item_needed}.")
        return False
    return True


def make_coffee(item):
    water_needed = MENU[item]["ingredients"]["water"]
    milk_needed = MENU[item]["ingredients"]["milk"]
    coffee_needed = MENU[item]["ingredients"]["coffee"]
    resources["water"] -= water_needed
    resources["milk"] -= milk_needed
    resources["coffee"] -= coffee_needed
    resources["money"] += MENU[user_input.lower()]["cost"]


def insert_coin(cost):
    sequence = [{"coin": "Quarters ($0.25)", "value": 0.25}, {"coin": "Dimes ($0.10)", "value": 0.1}, {"coin": "Nickles ($0.05)", "value": 0.05}, {"coin": "Pennies ($0.01)", "value": 0.01}]
    remain = cost
    total = 0
    for i in range(0, 4):
        print(f"Please insert coins: ${round(remain, 2)}")
        valid = False
        user_coin = ""
        while not valid:
            user_coin = input(f"{sequence[i]["coin"]}: ")
            try:
                user_coin = int(user_coin)
                valid = True
            except:
                print("Invalid input")
                valid = False

        remain -= user_coin * sequence[i]["value"]
        total += user_coin * sequence[i]["value"]
    return remain, total


user_input = ""
while user_input.lower() != "off":
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input.lower() == "report":
        print(
            f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")
    elif user_input.lower() == "espresso" or user_input.lower() == "latte" or user_input.lower() == "cappuccino":
        check = check_resources(user_input.lower())
        if not check:
            continue
        cost = MENU[user_input.lower()]["cost"]
        remain, total = insert_coin(cost)
        if total < cost:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total > cost:
            change = total - cost
            print(f"Here is ${round(change, 2)} dollars in change.")
        make_coffee(user_input.lower())
        print(f"Here is your {user_input.lower()}. Enjoy!")
