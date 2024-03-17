"""დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: 
კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი,
 ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე
   გადაყვანილი მნიშვნელობა. თუ მომხმარებელი 
სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision"."""

question1=input("please enter wich converter you need, mile to kilometre or kilometre to mile: ")

if question1 == "mile to kilometre":
    question2=int(input("please enter value of mile: "))
    kilometre=round(float(question2) * 2.62)
    print(kilometre, "km")

if question1 == "kilometre to mile":
    question3=int(input("please enter value of kilometre: "))    
    mile=round(float(question3) / 2.62)
    print(mile, "ml")


# print("1. km - miles")
# print("2. miles - km")

# choice = int(input('Please enter operation number (1 or 2): '))
# number = float(input("Please enter number to convert it: "))

# if choice == 1:
#     print(number / 1.6)
# elif choice == 2:
#     print(number * 1.6)
# else:
#     print("Wrong choice")

    

