#თანმიმდევრობა sequencing

#print("Tamo")
#print("Nika")
#print("Ana")

#იტერაცია, გამეორება, ციკლი - ietretion


#result = 0

#for i in range(5):
#   print("Tamo") 
#   result = result + 1

#print(result)    


# selections შერჩევა selection

#num=int(input("Please enter number in range 1-10: "))

#if num == 5:
#    print("You Won!")
#else:
#    print("You Lost!")

#Combination of iteration and selection
#for i in range(10):   # დიაპაზონს ქმნის 0 დან 10 მდე
#    if i % 2 == 0:
#        print(i, "is even")
#    else:
#        print(i, "is odd")


registered_password = "Tamo123"
authorized = False

while authorized != True:
   user_input = input("please enter yorr password: ")

   if user_input == registered_password:
       print("Accses granted!")
       authorized = True
   else:
       print("incorrect please try again")    
    
