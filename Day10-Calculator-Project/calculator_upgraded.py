import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


def modulo(n1, n2):
    return n1 % n2


def validate_number(variable):
    try:
        return float(variable)
    except ValueError:
        return None


def calculator():
    print(art.logo)

    def assign():
        ask_n1_again = True
        while ask_n1_again:
            n1 = input("Enter first number: ")
            n1 = validate_number(n1)
            if n1 is not None:
                ask_n1_again = False
            else:
                print("Invalid Input. Try again.")
        for j in calc_dict:
            print(j)

        ask_op_again = True
        while ask_op_again:
            op = input("Pick an operation: ")
            if op not in ['+', '-', '*', '/', '%', '**']:
                print("Invalid Input. Try Again.")
            else:
                ask_op_again = False

        ask_n2_again = True
        while ask_n2_again:
            n2 = input("Enter second number: ")
            n2 = validate_number(n2)
            if n2 is not None:
                ask_n2_again = False
            else:
                print("Invalid Input. Try again.")
        return n1, n2, op

    memory = []
    history = []

    def calc(n1, n2, op):
        if op in calc_dict.keys():
            chosen_op = calc_dict[op]
            try:
                ans = chosen_op(n1, n2)
            except ZeroDivisionError:
                print("Can't divide by zero.")
                return None
            except OverflowError:
                print("Result too large.")
                return None
            else:
                mem_item = f"{n1} {op} {n2} = {ans}"
                history.append(mem_item)
                print(mem_item)
                return ans
        else:
            print("Invalid Input.")
            return None

    calc_dict = {
        "+": add,
        "-": sub,
        "*": multiply,
        "/": divide,
        "**": power,
        "%": modulo
    }

    no_of_calcs = 0
    num1, num2, operation = assign()
    print('\n')
    result = calc(num1, num2, operation)
    print('\n')
    print("*************************************************************************************************\n")

    no_of_calcs += 1
    restart = True
    while restart:
        choice = input(f"""1. Do you want to continue calculating with {result}?
2. Do you want to start a new calculation?
3. View total no.of calculations performed
4. Store in memory
5. Recall memory
6. Clear memory
7. View History
8. Quit the program
Pick the number against your choice: """).strip()
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                num1 = result
                for i in calc_dict:
                    print(i)

                ask_opn_again = True
                while ask_opn_again:
                    operation = input("Pick an operation: ")
                    if operation not in ['+', '-', '*', '/', '%', '**']:
                        print("Invalid Input. Try again.")
                        ask_opn_again = True
                    else:
                        ask_opn_again = False

                ask_num2_again = True
                while ask_num2_again:
                    num2 = input("Enter second number: ")
                    num2 = validate_number(num2)

                    if num2 is None:
                        print("Invalid Input. Try again.")
                        ask_num2_again = True
                    else:
                        ask_num2_again = False

                print('\n')
                result = calc(num1, num2, operation)
                print('\n')
                print("*************************************************************************************************\n")
                no_of_calcs += 1

            elif choice == 2:
                num1, num2, operation = assign()
                print('\n')
                result = calc(num1, num2, operation)
                print('\n')
                print("*************************************************************************************************\n")
                no_of_calcs += 1

            elif choice == 3:
                print(f"\nTotal calculations performed: {no_of_calcs}\n")
                print("*************************************************************************************************\n")

            elif choice == 4:
                print("\nStored result in memory.\n")
                memory.append(f"{num1} {operation} {num2} = {result}")
                print("*************************************************************************************************\n")

            elif choice == 5:
                if len(memory) != 0:
                    print("\nCalculator memory: ")
                    for i in memory:
                        print(i)
                    print("*************************************************************************************************")
                    print("\n")
                else:
                    print("\nCalculator memory is empty.\n")
                    print("*************************************************************************************************\n")

            elif choice == 6:
                if len(memory) == 0:
                    print("\nCalculator memory is empty.\n")
                    print("*************************************************************************************************\n")

                elif len(memory) != 0:
                    print("\nMemory cleared.\n")
                    memory.clear()
                    print("*************************************************************************************************\n")

            elif choice == 7:
                print("\nCalculator History: ")
                for k in history:
                    print(k)
                print("*************************************************************************************************")
                print("\n")

            elif choice == 8:
                restart = False
                print("\nCalculator Program Exited.")
                print("*************************************************************************************************")

            else:
                print("\nInvalid Input. Try again.\n")

        else:
            print("\nInvalid Input. Try again.\n")
    return None


calculator()
