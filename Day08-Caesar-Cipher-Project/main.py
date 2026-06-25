from art import logo


lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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

    print(f"""Here is the {encode_decode}d text: {output_text}
Characters encrypted/decrypted = {characters_encrypted}
Spaces preserved = {spaces_preserved}
Symbols preserved = {symbols_preserved}""")


print(logo)
should_continue = True

while should_continue:
    choice = int(input("""What do you want to do?
1. Encode
2. Decode
3. Exit
Type the index number: """))

    if choice == 1:
        direction = 'encode'
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_decode=direction)
        should_continue = True

    elif choice == 2:
        direction = 'decode'
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_decode=direction)
        should_continue = True

    elif choice == 3:
        should_continue = False
        print("Goodbye!")

    else:
        print("Invalid Input. Try Again.")
        should_continue = True