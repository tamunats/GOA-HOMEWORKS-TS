"""ტემპერატურის კლასიფიკაცია: შექმენით პროგრამა, რომელიც 
მომხმარებელს სთხოვს ტემპერატურას ცელსიუსში. შემდეგ დაბეჭდეთ 
ცხელი (> 30°C), თბილი (20-30°C) ან ცივი (<20°C)."""

enter_temperature=int(input("plese enter temperatura in °C "))

if enter_temperature > 30:
    print("It is hot")
if enter_temperature < 20:
    print("it is cold")
else:
    print("it is warm")