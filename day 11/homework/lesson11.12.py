"""რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. 
სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან"""

enter_number=int(input("please enter number "))

while enter_number % 2 != 0:
    enter_number=int(input("please enter number "))