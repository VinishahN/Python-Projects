from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()

# coffee.report()
# money.report()
should_continue = True
while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in menu.get_items():
        order_name = menu.find_drink(order)
        existence = coffee.is_resource_sufficient(order_name)
        if existence:
            payment = money.make_payment(order_name.cost)
            if payment:
                   coffee.make_coffee(order_name)
    elif order == "report":
        coffee.report()
        money.report()
    else:
        should_continue = False

