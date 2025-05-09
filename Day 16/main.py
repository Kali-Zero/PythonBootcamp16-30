from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ")
    if choice == "off":
        is_on = False
    #Print Report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #2 Check resources sufficient?, # 3 Process coins, #4 Check transaction successful?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # 5 Make Coffee
            coffee_maker.make_coffee(drink)
