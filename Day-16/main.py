from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_make = CoffeeMaker()
money_mach = MoneyMachine()
menu = Menu()

while True:
    need = input("What would you like? (espresso/latte/cappuccino): ")

    if need == "report":
        coffee_make.report()
        money_mach.report()
    elif need == "off":
        break
    else:
        drink = menu.find_drink(need)
        if coffee_make.is_resource_sufficient(drink) and money_mach.make_payment(drink.cost):
            coffee_make.make_coffee(drink)