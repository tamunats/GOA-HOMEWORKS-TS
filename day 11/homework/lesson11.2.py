"""რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს 
სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს.
 შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი."""


# num = 0

# enter_number=int(input("please enter number "))
# sum=0

# while enter_number != num:
#     enter_number=int(input("please enter number "))
#     sum=sum + enter_number

# print(sum)


num = 0
sum = 0
 # true იმიტო ვწერთ რომ ლუპმა სამუდამოდ იმუშაოს 
#იმ შემთხვევაში თუ შემოტანილი რიცხვი არ უდრის რიხვს
#(მხოლოდ იმ შემთხვევაში გაჩერდება თუ რიცხვი უდრის და კოდი break თან მივა)
while True:  
    enter_number=int(input("please enter number "))
    if enter_number == num:
        break    #წყვიტავს ციკლს
    sum += enter_number  # იგივეა sum=sum + enter_number

print("sum of the enter number: ", sum)    