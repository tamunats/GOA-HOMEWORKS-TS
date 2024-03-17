"""1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
If the age is less than 18, print "You are a minor."
If the age is between 18 and 65, print "You are an adult."
If the age is 65 or older, print "You are a senior citizen."""


age=int(input("please enter your age: "))

if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")        