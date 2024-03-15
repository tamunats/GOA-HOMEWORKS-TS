"""მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა."""

year=int(input("please enter year: "))

if year % 4 == 0 and year % 100 != 0:
    print(year, "is leap year")

if year % 4 > 0:
    print(year, "is not leap year")
 






