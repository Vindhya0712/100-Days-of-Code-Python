import menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import prettytable


menu_items = menu.Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

continue_machine = True
while continue_machine:
    print("Welcome to PyCoffee: A Coffee Machine!")
    user_choice = input(f"What would you like to have? ({menu_items.get_items()}report/off): ").lower().strip()

    if user_choice == 'off':
        continue_machine = False
        print("Goodbye!👋 \nMachine turned off.")
    elif user_choice == 'report':
        report_table = prettytable.PrettyTable()
        report_table.field_names = ['Resources', 'Available']

        report_table.add_row(['Water', f"{coffee_maker_obj.resources['water']}ml"])
        report_table.add_row(['Milk', f"{coffee_maker_obj.resources['milk']}ml"])
        report_table.add_row(['Coffee', f"{coffee_maker_obj.resources['coffee']}g"])
        report_table.add_row(['Money', f"${money_machine_obj.profit:.2f}"])
        report_table.align = 'l'

        print('\n')
        print('=' * 30)
        print('☕ Coffee Machine Report ☕')
        print('=' * 30)
        print(f"{report_table}\n")
    else:
        drink_name = menu_items.find_drink(user_choice)
        if drink_name is not None:
            if coffee_maker_obj.is_resource_sufficient(drink=drink_name) is True:
                if money_machine_obj.make_payment(drink_name.cost):
                    coffee_maker_obj.make_coffee(drink_name)
