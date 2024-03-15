"""მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for 
ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. 
ციკლში იტერაცია მოახდინეთ ერთით
 და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი)."""

num1=int(input("please enter first number: "))
num2=int(input("please enter second number: "))

if num1 < num2:
    for i in range(num1 - 1, num2):
        i=i + 1
        print(i**3)

if num2 <num1:
    for i in range(num2 -1, num1):
        i=i + 1
        print(i**3)        