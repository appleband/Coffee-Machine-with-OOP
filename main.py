from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()


while True:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'report':
        coffee.report()
        money.report()
    elif order == 'off':
        exit()
    else:
        valid_menu_item = menu.find_drink(order)
        if valid_menu_item is not None:
            make_cup = coffee.is_resource_sufficient(valid_menu_item)
            if make_cup:
                transaction = money.make_payment(valid_menu_item.cost)
                if transaction:
                    coffee.make_coffee(valid_menu_item)

