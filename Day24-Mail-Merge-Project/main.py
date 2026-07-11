#TODO: Create a letter using starting_letter.txt
with open('Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()

print(letter)
#for each name in invited_names.txt
list_of_names = []
with open('Input/Names/invited_names.txt', 'r') as f:
    names = f.readlines()
    for i in names:
        i = i.strip('\n')
        list_of_names.append(i)

print(list_of_names)

#Replace the [name] placeholder with the actual name.
files = {}

for i in range(len(list_of_names)):
    name_of_person = list_of_names[i]
    new_letter = letter.replace('[name]', name_of_person)
    print(new_letter)
    filename = f'letter_for_{name_of_person}.txt'
    files[filename] = new_letter
#Save the letters in the folder "ReadyToSend".
for key in files:
    with open(f'Output/ReadyToSend/{key}', 'w') as personalized_letter:
        personalized_letter.write(f'{files[key]}')
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp