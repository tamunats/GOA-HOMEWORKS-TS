"""2) მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ შემოტანილი რიცხვი,
 თუ რიცხვი მეტია ნულზე მაშინ დავუბეჭდოთ რომ რიცხვი არის დადებით,
   სხვა შემთხვევაში თუ რიცხვი ნაკლებია ნნულზე დავუბეჭდოთ რომ რიცხვი არის უარყოფითი,
 ხოლო სხვა შემთხვევაში დაბეჭდეთ რომ რიცხვი არის 0"""


enter_number=int(input("please enter number"))

if enter_number > 0:
    print("number is positive")
elif enter_number < 0:
    print("number is negative") 
else:
    print("numer equals 0")    