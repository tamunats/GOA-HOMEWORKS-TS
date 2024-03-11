"""რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი
 (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა,
   სანამ არ გამოიცნობენ სწორად."""

num = 5

enter_number=int(input("please enter number "))

while enter_number != num:
    enter_number=int(input("please enter number "))
