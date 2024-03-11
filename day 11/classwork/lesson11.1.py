"""მომხმარებელს შეეკითხეთ საკუთარი ასაკი თუ ის აღემატება 18-ს გამოიტანეთ რომ სრულწლოვანის,
სხვა შემთხვევაში დაბეჭდეთ რომ ბავშვია"""

age=int(input("Enter your age "))

if age > 18:
    print("You are an adult")
else:
    print("you are a child")