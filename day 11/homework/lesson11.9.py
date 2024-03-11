"""შეამოწმეთ გაყოფა: შექმენით პროგრამა,
 რომელიც მომხმარებელს სთხოვს რიცხვს. შემდეგ დაბეჭდეთ,
 იყოფა თუ არა 2-ზე, 3-ზე ან ორივეზე."""

enter_number=int(input("please enter number "))

if enter_number % 2 == 0:
    print("The number is divisible by 2")
else:
    print("The number is not divisible 2")    
if enter_number % 3 == 0:
    print("The number is divisible by 3")  
else:
    print("Tne number is not divisible by 3")      


     