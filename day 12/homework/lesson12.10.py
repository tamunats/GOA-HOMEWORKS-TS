"""დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება 
თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის."""


enter_text1=input("please enter text: ")
enter_number=int(input("how many times repeat this text? "))

for i in range (enter_number):
   print(enter_text1)
