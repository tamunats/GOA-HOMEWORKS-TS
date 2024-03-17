"""3) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს 
შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ 
დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."""


point=input("please enter you exam point (A, B, C, D or F): ")

if point == "A":
    print("Excellent!")
elif point == "B":
    print("Good job!")   
elif point == "C":
    print("You passed.")
elif point == "D":
    print("You can do better.")
else:
    print("You failed.")      
