"""პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც 
სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა,
 სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678"."""




# registered_password = "12345678"
# authorized = False

# while authorized != True:
#    user_input = input("please enter yorr password: ")

#    if user_input == registered_password:
#        print("Accses granted!")
#        authorized = True
#    else:
#        print("incorrect please try again")     
    

correct_pasword="12345678"
user_password=input("enter a password ")
while user_password != correct_pasword:
    print("wrong try again")
    user_password=input("enter a password ")
