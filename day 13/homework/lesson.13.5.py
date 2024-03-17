"""5) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. 
გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, 
სანამ მომხმარებელი სწორად არ გამოიცნობს"""

i=5
enter_number=int(input("please enter number from 1 to 10: "))
while enter_number != i:
    enter_number=int(input("please enter number from 1 to 10: "))