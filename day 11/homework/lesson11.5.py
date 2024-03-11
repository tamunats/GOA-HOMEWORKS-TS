"""დადებითი რიცხვები: შექმენით პროგრამა, რომელიც სთხოვს 
მომხმარებელს უწყვეტად შეიყვანოს დადებითი რიცხვები, სანამ ისინი
 უარყოფით რიცხვს არ შეიყვანენ. შემდეგ დაბეჭდეთ ყველა შეყვანილი
 დადებითი რიცხვის ჯამი. """


num = 0
enter_number=int(input("please enter number "))
sum= 0
while enter_number >= 0:
    enter_number=int(input("please enter number "))
    if enter_number >= 0:
        sum=sum + enter_number
    
       
print(sum)  