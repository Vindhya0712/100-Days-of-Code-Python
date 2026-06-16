print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10/12/15 "))
people = int(input("How many people to split the bill? "))

total = round(bill + bill * tip/100, 2)
per_person = total/people
print(f"Total bill is ${total}")
print(f"Each person has to pay ${per_person}")
