from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_make = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_make.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_make.make_coffee(drink)
