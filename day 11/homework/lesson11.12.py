"""რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. 
სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან"""

enter_number=int(input("please enter number "))

num=enter_number
while num % 2 == 0:
     enter_number=int(input("please enter number "))
