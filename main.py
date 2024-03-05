from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

user_input = ""
while not user_input == "off":
    user_input = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    options = menu.get_items()
    if user_input == "off":
        continue
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(user_input):
            drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
