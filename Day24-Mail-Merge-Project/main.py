with open('Input/Letters/starting_letter.txt', 'r') as file:
    letter = file.read()

list_of_names = []
with open('Input/Names/invited_names.txt', 'r') as f:
    names = f.readlines()
    for i in names:
        i = i.strip('\n')
        list_of_names.append(i)

files = {}

for i in range(len(list_of_names)):
    name_of_person = list_of_names[i]
    new_letter = letter.replace('[name]', name_of_person)
    filename = f'letter_for_{name_of_person}.txt'
    files[filename] = new_letter

for key in files:
    with open(f'Output/ReadyToSend/{key}', 'w') as personalized_letter:
        personalized_letter.write(f'{files[key]}')

print("Personalized letters generated!")
