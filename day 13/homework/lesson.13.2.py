"""2) შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ
 დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს
 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი."""



for i in range (5):
    num=int(input("please enter number: "))
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")    

