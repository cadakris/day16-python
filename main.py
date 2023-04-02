from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''This will create the object'''
ingredients_report = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True


'''This will print out total profits and ingredient report'''


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        ingredients_report.report()
    else:
        drink = menu.find_drink(choice)
        if ingredients_report.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                ingredients_report.make_coffee(drink)






