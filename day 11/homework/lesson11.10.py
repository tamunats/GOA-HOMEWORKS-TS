"""რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს
 მომხმარებელს ორ რიცხვს და შეადარებს მათ."""

enter_num1=int(input("please enter number "))
enter_num2=int(input("please enter number "))
num1 = enter_num1
num2 = enter_num2

if enter_num1 > enter_num2:
    print(num1, ">",  num2)
if enter_num1 < enter_num2: 
    print(num1, "<", num2)   
if enter_num1 == enter_num2:
    print(num1, "=", num2)    