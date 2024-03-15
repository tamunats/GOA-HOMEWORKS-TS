"""რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ 
ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე,
 დაპრინტეთ ის და მასზე მოახდინეთ იტერაცია 1-ით."""

enter_number=int(input("please enter number "))
number_after_addition=enter_number + 20

while enter_number < number_after_addition:
    print(enter_number)
    enter_number=enter_number + 1 