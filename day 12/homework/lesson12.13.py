"""დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს 
შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. თუ რიცხვი არის 1-ზე 
ნაკლები ან 5-ზე მეტი, დაბეჭდეთ "Invalid input".
 თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input"""


enter_number=int(input("please enter number for 1 to 5: "))


if enter_number < 1 or enter_number > 5:
    print("invalid input")
if enter_number >= 1 and enter_number <= 5:  
    print("valid input")
  