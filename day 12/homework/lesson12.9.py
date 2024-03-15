"""შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება).
 მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ 
ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას."""


enter_number1=float(input("please enter first numer: "))
enter_number2=float(input("please enter second number: "))
operation=input("which operation you need addition, deduction, division or multiply? ")

if operation == "addition":
    print(enter_number1 + enter_number2)
if operation == "deduction":
    print(enter_number1 - enter_number2)
if operation == "division":
    print(enter_number1 / enter_number2)
if operation == "multiply":
    print(enter_number1 * enter_number2)          