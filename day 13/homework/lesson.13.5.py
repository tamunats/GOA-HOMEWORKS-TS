"""5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. 
გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, 
სანამ მომხმარებელი სწორად არ გამოიცნობს"""

i=5
enter_number=int(input("please enter number from 1 to 10: "))
while enter_number != i:
    enter_number=int(input("please enter number from 1 to 10: "))




num = 4
count = 0
number = 0

while number != num:
    number = int(input("Please enter number (1-10): "))
    count = count + 1
    if number == num:
        print("You guessed number in",count,"try")