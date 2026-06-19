import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def reconstruct_dictionary():
    stored_passwords = {}
    with open("Password Manager.txt", 'a+') as f:
        for string in f.readlines():
            a_name, _, p_stored = string.partition(':')
            pass_stored = ''
            if '\n' in p_stored:
                for i in p_stored:
                    if i != '\n':
                        pass_stored += i
                stored_passwords[a_name] = pass_stored
            else:
                stored_passwords[a_name] = p_stored
    return stored_passwords


def store_new_entries(dictionary, password_to_store):
    a_name = input("Enter account name: ").lower()
    if a_name in dictionary:
        print(f"Replacing old password for {a_name}")
        dictionary[a_name] = password_to_store
        return dictionary
    else:
        print("Storing password in program memory.")
        dictionary[a_name] = password_to_store
        return dictionary


def update_memory(dictionary):
    with open("Password Manager.txt", 'w') as f:
        for account in dictionary:
            f.write(f"{account}:{dictionary[account]}\n")


def display_password_info(password_to_analyze):
    length = len(password_to_analyze)
    if length < 8:
        print(f"Password length: {length}\nPassword Strength: Weak\n")
    elif length <= 12:
        print(f"Password length: {length}\nPassword Strength: Medium\n")
    else:
        print(f"Password length: {length}\nPassword Strength: Strong\n")


def generate_password(nl, ns, nn):
    password_lst = []
    for i in range(nl):
        password_lst.append(random.choice(letters))

    for i in range(ns):
        password_lst.append(random.choice(symbols))

    for i in range(nn):
        password_lst.append(random.choice(numbers))

    random.shuffle(password_lst)
    password_char = ""
    for i in password_lst:
        password_char += i
    return password_char


def password_generator():
    print("Welcome to the PyPassword Generator!")
    ask_again = True

    while ask_again:
        choice = int(input("""What do you want to do?
1. Generate a new password
2. Retrieve Old Passwords
3. Display program memory
4. Exit
Type your choice: """))

        if choice == 1:
            password_manager = reconstruct_dictionary()

            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            nr_numbers = int(input(f"How many numbers would you like?\n"))

            password = generate_password(nr_letters, nr_symbols, nr_numbers)
            print(f"\nYour password is: {password}")
            # Display info about the generated password
            display_password_info(password)

            # Ask user if they want to generate another password with same settings
            generate_again = True
            new_password = password
            while generate_again:
                again = input("Generate another password with the same settings? Y/N: ").upper()
                if again == 'Y':
                    new_password = generate_password(nr_letters, nr_symbols, nr_numbers)
                    print(f"\nNew password: {new_password}")
                    # Display info about new password
                    display_password_info(new_password)

                else:
                    generate_again = False
                    store_password = input("Do you want to store this password? Y/N: ").upper()
                    if store_password == 'Y':
                        store_new_entries(password_manager, new_password)
                        update_memory(password_manager)
                        break
                    else:
                        print("Password not stored.")
                        update_memory(password_manager)
                        break

        elif choice == 2:
            password_manager = reconstruct_dictionary()
            account_name = input("Which account's password do you want to retrieve? \n").lower()
            if account_name in password_manager:
                password = password_manager[account_name]
                print(f"The password for {account_name} is {password}")
                update_memory(password_manager)
            else:
                print("The account does not exist in the memory.")
                store = input("Do you want to store a password for this account? Y/N: ").upper()
                if store == 'Y':
                    password = input("What's the password for this account? ")
                    password_manager[account_name] = password
                    update_memory(password_manager)

        elif choice == 3:
            password_manager = reconstruct_dictionary()
            print("\nData stored in program memory: \n")
            for account in password_manager:
                print(f"{account}:{password_manager[account]}")
            print("\n")

        else:
            password_manager = reconstruct_dictionary()
            print("Turning off the program")
            update_memory(password_manager)
            ask_again = False


password_generator()
