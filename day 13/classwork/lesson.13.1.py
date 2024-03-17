
"""შემოატანინეთ მომხმარებელს თავისი ასაკი input  ფუნქციის გამოყენებით
 შემდეგ შეამოწმეთ ასაკი არის თუ არა  მეტი  ან უდრის0 და ნაკლები 18 ზე დაუბეჭდეთ რომ არის ბავშვი
   სხვა შემთხვევაში მეტია ან უდრის18 ზე და ნაკლებია 50 ზე დავუბეჭდოთ რომ 
არის ზრდასრული სხვა შემთხვევაში ის არის მოხუცი"""

enter_age=int(input("please enter your age: "))

if enter_age >= 0 and enter_age < 18:
    print("you are child")
elif enter_age >= 18 and enter_age < 50:
    print("you are adult")
else:
    print("you are old")        