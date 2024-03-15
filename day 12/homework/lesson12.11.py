"""დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის 
ინდექსს (BMI), მომხმარებლისგან მიღებული წონის (კილოგრამებში)
 და სიმაღლის (მეტრებში) გათვალისწინებით. 
"""
# MBI=წონა(კგ)/სიმაღლე(მ2)

height=float(input("please enter height in centimeters: "))
kilogram=float(input("please enter weight in kilograms: "))

height_m2=(height / 100) * (height / 100)

BMI=kilogram / height_m2

print("your BMI is " , BMI)

