from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    coffee_bot = CoffeeMaker()
    coffee_menu = Menu()
    coffee_money = MoneyMachine()
    machine_on = True
    while machine_on:
        coffee_choice = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
        if coffee_choice == "report":
            coffee_bot.report()
            coffee_money.report()
        else:
            item = coffee_menu.find_drink(coffee_choice)
            if coffee_bot.is_resource_sufficient(item) == True:
                if coffee_money.make_payment(item.cost) == True:
                    coffee_bot.make_coffee(item)

            else:
                print(coffee_bot.is_resource_sufficient(item))



coffee_machine()