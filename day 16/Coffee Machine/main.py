from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
maker = CoffeeMaker()
money_machine = MoneyMachine()
# coffee = coffee_menu.get_items().split('/')

while True:
    choice = input(f"What do would you like ({coffee_menu.get_items()}): ").lower()
    
    print(coffee_menu.find_drink(choice))

