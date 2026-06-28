import prettytable

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def validate_integer(variable):
    if variable.isdigit():
        return int(variable)
    else:
        return None


def display_menu():
    m_table = prettytable.PrettyTable()

    m_table.field_names = ['Sl No.', 'Item', 'Cost']

    m_table.add_row(['1', 'espresso', f"${MENU['espresso']['cost']:.2f}"])
    m_table.add_row(['2', 'latte', f"${MENU['latte']['cost']:.2f}"])
    m_table.add_row(['3', 'cappuccino', f"${MENU['cappuccino']['cost']:.2f}"])
    m_table.add_row(['4', 'report', '--'])
    m_table.add_row(['5', 'off', '--'])

    m_table.align = 'l'
    return m_table


def resources_needed(drink):
    w_need, m_need, c_need = 0, 0, 0
    for i in MENU[drink]['ingredients']:
        if i == 'water':
            w_need += MENU[drink]['ingredients'][i]
        if i == 'milk':
            m_need += MENU[drink]['ingredients'][i]
        if i == 'coffee':
            c_need += MENU[drink]['ingredients'][i]
    return w_need, m_need, c_need


def check_resources_suff(drink):
    w_needed, m_needed, c_needed = resources_needed(drink)
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if water >= w_needed and milk >= m_needed and coffee >= c_needed:
        return True
    else:
        lst = []
        if water < w_needed:
            lst.append('water')
        if milk < m_needed:
            lst.append('milk')
        if coffee < c_needed:
            lst.append('coffee')

        if len(lst) == 1:
            print(f"Sorry, there wasn't enough {lst[0]} 😓")
        elif len(lst) == 2:
            print(f"Sorry, there wasn't enough {lst[0]} and {lst[1]} 😓")
        elif len(lst) == 3:
            print(f"Sorry, there wasn't enough {lst[0]}, {lst[1]} and {lst[2]} 😓")

        return False

def process_coins(drink):
    is_true = check_resources_suff(drink)
    ask_again = True
    while ask_again:
        if is_true:
            print(f"The {drink} costs ${MENU[drink]['cost']}. Please enter coins.")
            q = input("How many quarters? ")
            d = input("How many dimes? ")
            n = input("How many nickles? ")
            p = input("How many pennies? ")

            quarters = validate_integer(q)
            dimes = validate_integer(d)
            nickles = validate_integer(n)
            pennies = validate_integer(p)

            if quarters is not None and dimes is not None and nickles is not None and pennies is not None:
                    money_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
                    cost = MENU[drink]['cost']

                    if money_inserted < cost:
                        print("Sorry, that wasn't enough money 😭. Money refunded. 💸")
                        again = input("1. Try again\n"
                                      "2. Cancel purchase\n"
                                      "Enter your choice: ")
                        again = validate_integer(again)

                        if again == 1:
                            ask_again = True
                        else:
                            print("Purchase cancelled. You can order another drink now.")
                            ask_again = False

                    elif money_inserted == cost:
                        print(f"Here is your {drink}. Enjoy! ☕")
                        ask_again = False
                        return True
                    else:
                        change = round((money_inserted - cost), 2)
                        print(f"Here is ${change:.2f} in change 🪙. Enjoy your {drink}! ☕")
                        ask_again = False
                        return True
            else:
                lst = []
                if quarters is None:
                    lst.append('quarters')
                if dimes is None:
                    lst.append('dimes')
                if nickles is None:
                    lst. append('nickles')
                if pennies is None:
                    lst.append('pennies')


                if len(lst) == 1:
                    print(f"Invalid Input for {lst[0]}")
                elif len(lst) == 2:
                    print(f"Invalid Input for {lst[0]} and {lst[1]}")
                elif len(lst) == 3:
                    print(f"Invalid Input for {lst[0]}, {lst[1]}, and {lst[2]}")
                else:
                    print(f"Invalid Input for {lst[0]}, {lst[1]}, {lst[2]} and {lst[3]}")

                again = input("1. Try again\n"
                              "2. Cancel purchase\n"
                              "Enter your choice: ")
                again = validate_integer(again)

                if again == 1:
                    ask_again = True
                else:
                    print("Cancelling purchase. Refunding any money inserted 💸")
                    ask_again = False
    return None


def deduct_resources(drink, w, m, c):
    if check_resources_suff(drink):
        w_needed, m_needed, c_needed = resources_needed(drink)
        w -= w_needed
        m -= m_needed
        c -= c_needed
        return w, m, c
    else:
        return w, m, c


def make_drink(drink, w, m, c):
    cash = resources['money']
    if check_resources_suff(drink):
        if process_coins(drink):
            w_left, m_left, c_left = deduct_resources(drink, w, m, c)
            cash += MENU[drink]['cost']
            resources['water'] = w_left
            resources['milk'] = m_left
            resources['coffee'] = c_left
            resources['money'] = cash

            return resources
    else:
        return resources


def get_report(w, m, c, cash):
    report_table = prettytable.PrettyTable()

    report_table.field_names = ['Resources', 'Available']

    report_table.add_row(['Water', f"{w}ml"])
    report_table.add_row(['Milk', f"{m}ml"])
    report_table.add_row(['Coffee', f"{c}g"])
    report_table.add_row(['Money', f"${cash:.2f}"])

    report_table.align = 'l'
    print(f"\n{report_table}")


def coffee_machine(resource_list):
    print("Welcome to PyCoffee -- A Coffee Machine!")
    menu_table = display_menu()
    user_choice = input(f"Here is our menu. What would you like to have?\n{menu_table}\nType your choice 📝: ")
    choice = validate_integer(user_choice)
    water = resource_list['water']
    milk = resource_list['milk']
    coffee = resource_list['coffee']
    money = resource_list['money']

    if choice is not None:
        if choice == 1:
            drink_name = 'espresso'
            updated_resource_list = make_drink(drink_name, water, milk, coffee)
            resource_list = updated_resource_list
            return True

        elif choice == 2:
            drink_name = 'latte'
            updated_resource_list = make_drink(drink_name, water, milk, coffee)
            resource_list = updated_resource_list
            return True

        elif choice == 3:
            drink_name = 'cappuccino'
            updated_resource_list = make_drink(drink_name, water, milk, coffee)
            resource_list = updated_resource_list
            return True

        elif choice == 4:
            get_report(water, milk, coffee, money)
            return True

        elif choice == 5:
            print("Turning off machine\nGoodbye! 👋")
            return False

        else:
            print("❌ Invalid Input. Please try entering the serial number against your choice.")
            return True

    else:
        print("❌ Invalid Input. Please try entering the serial number against your choice.")
        return True


continue_machine = True
while continue_machine:
    continue_machine = coffee_machine(resources)
    print('\n')
    print(f"{'-' * 100}\n")
