"""დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, 
უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი."""

enter_number=int(input("please enter number "))

if enter_number > 0:
    print("number is positive")
if enter_number < 0:
    print("number is negative")    
if enter_number == 0:
    print("number equals zero")