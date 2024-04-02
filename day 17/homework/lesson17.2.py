"""2)შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, 
შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, 
ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს"""

enter_num1=int(input("please enter num: "))
enter_num2=int(input("please enter num: "))
enter_num3=int(input("please enter num: "))
enter_num4=int(input("please enter num: "))
enter_num5=int(input("please enter num: "))

num1=enter_num1
num2=enter_num2
num3=enter_num3
num4=enter_num4
num5=enter_num5

list=[num1, num2, num3, num4, num5]

if num1 % 2 == 0:
    print(num1)
elif num2 % 2 == 0:
    print(num2)
elif num3 % 2 == 0:
    print(num3)
elif num4 % 2 == 0:
    print(num4)
elif num5 % 2 == 0:
    print(num5)


