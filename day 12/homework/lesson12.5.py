"""მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე 
რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ 
ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში."""

num=int(input("please enter number from 1 to 9: "))


for i in range(num, 50 +1, num):
    print(i)