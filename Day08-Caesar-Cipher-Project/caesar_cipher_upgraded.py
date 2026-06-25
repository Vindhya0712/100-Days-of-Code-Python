from art import logo

counter = 0
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']


def Caesar_Cipher_Project():
    def save_session_history_to_file(input_list):
        with open("Caesar Cipher Program History.txt", 'a+') as file:
            for i in input_list:

                if i['saved'] is False:

                    if 'characters_encrypted' in i.keys():
                        file.write(f"""\n-------------------------SESSION SAVED-----------------------------------
    Operation: {i['operation']}
    Shift Number: {i['shift']}

    Original Text: {i['original_text']}
    Result Text: {i['result']}

    Encrypted characters: {i['characters_encrypted']}
    Spaces preserved: {i['spaces_preserved']}
    Symbols preserved: {i['symbols_preserved']}
    Numbers preserved: {i['numbers_preserved']}
    --------------------------------------------------------------------------\n""")
                        i['saved'] = True

                    else:
                        file.write(f"""\n----------------------------SESSION SAVED----------------------------------
    Operation: {i['operation']}
    Shift Number: {i['shift']}

    Original Text: {i['original_text']}
    Result Text: {i['result']}

    Decrypted characters: {i['characters_decrypted']}
    Spaces preserved: {i['spaces_preserved']}
    Symbols preserved: {i['symbols_preserved']}
    Numbers preserved: {i['numbers_preserved']}
    --------------------------------------------------------------------------\n""")
                        i['saved'] = True

    def view_session_history(input_list):
        for i in input_list:
            if 'characters_encrypted' in i.keys():
                print(f""" ---------------------------------------------------------------------------------------------
Operation: {i['operation']}
Shift Number: {i['shift']}

Original Text: {i['original_text']}
Result Text: {i['result']}

Encrypted characters: {i['characters_encrypted']}
Spaces preserved: {i['spaces_preserved']}
Symbols preserved: {i['symbols_preserved']}
Numbers preserved: {i['numbers_preserved']}
--------------------------------------------------------------------------------------------------------------------""")

            else:
                print(f"""----------------------------------------------------------------------------------------------
Operation: {i['operation']}
Shift Number: {i['shift']}

Original Text: {i['original_text']}
Result Text: {i['result']}

Decrypted characters: {i['characters_decrypted']}
Spaces preserved: {i['spaces_preserved']}
Symbols preserved: {i['symbols_preserved']}
Numbers preserved: {i['numbers_preserved']}
--------------------------------------------------------------------------------------------------------------------""")

    def caesar(original_text, shift_amount, encode_decode):
        output_text = ''
        if encode_decode == "decode":
            shift_amount = shift_amount * (-1)

        characters_encrypted = 0
        symbols_preserved = 0
        spaces_preserved = 0
        numbers_preserved = 0

        for letter in original_text:

            if letter.islower():
                shifted_position = lower_alphabet.index(letter) + shift_amount
                shifted_position %= len(lower_alphabet)
                output_text += lower_alphabet[shifted_position]
                characters_encrypted += 1

            elif letter.isupper():
                shifted_position = upper_alphabet.index(letter) + shift_amount
                shifted_position %= len(upper_alphabet)
                output_text += upper_alphabet[shifted_position]
                characters_encrypted += 1

            else:
                if letter == ' ':
                    output_text += letter
                    spaces_preserved += 1
                else:
                    if letter.isdigit():
                        output_text += letter
                        numbers_preserved += 1
                    else:
                        output_text += letter
                        symbols_preserved += 1

        print(f"""\nHere is the {encode_decode}d text: {output_text}\n""")

        return output_text, characters_encrypted, spaces_preserved, symbols_preserved, numbers_preserved

    total_messages = 0
    total_encryptions = 0
    total_decryptions = 0
    run_history = []

    def manage_data(choice12, tmessages, tencryption, tdecryption, input_list):

        if choice12 == 1:
            direction = 'encode'
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            output, characters, spaces, symbols, numbers = caesar(original_text=text, shift_amount=shift,
                                                                  encode_decode=direction)
            tmessages += 1
            tencryption += 1
            entry = {}
            entry['operation'] = 'encode'
            entry['shift'] = shift
            entry['original_text'] = text
            entry['result'] = output
            entry['characters_encrypted'] = characters
            entry['spaces_preserved'] = spaces
            entry['symbols_preserved'] = symbols
            entry['numbers_preserved'] = numbers
            entry['saved'] = False
            input_list.append(entry)

        elif choice12 == 2:
            direction = 'decode'
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            output, characters, spaces, symbols, numbers = caesar(original_text=text, shift_amount=shift,
                                                                  encode_decode=direction)
            tmessages += 1
            tdecryption += 1
            entry = {}
            entry['operation'] = 'decode'
            entry['shift'] = shift
            entry['original_text'] = text
            entry['result'] = output
            entry['characters_decrypted'] = characters
            entry['spaces_preserved'] = spaces
            entry['symbols_preserved'] = symbols
            entry['numbers_preserved'] = numbers
            entry['saved'] = False
            input_list.append(entry)

        elif choice12 == 3:
            print('\n')
            return input_list


        elif choice12 == 4:
            print("\n Saving into program memory\n")
            return input_list

    print(logo)
    should_continue = True

    while should_continue:
        choice = int(input("""What do you want to do? 
1. Encode
2. Decode
3. View Session History
4. Save Session History
5. Exit
Type the index number: """))

        if choice in [1, 2, 3, 4]:
            history_list = manage_data(choice, total_messages, total_encryptions, total_decryptions, run_history)
            if choice == 3:
                history_list = manage_data(choice)
                if len(history_list) == 0:
                    print("\nThere isn't any session history yet!\n")
                else:
                    view_session_history(history_list)

            elif choice == 4:
                if len(history_list) == 0:
                    print("\nThere isn't any session history yet!\n")
                else:
                    save_session_history_to_file(history_list)

        elif choice == 5:
            print("Goodbye!")
            should_continue = False

        else:
            print("Invalid Input. Try Again")


Caesar_Cipher_Project()
