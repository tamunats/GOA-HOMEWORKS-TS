"""რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის 
ჩათვლით გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი,
 სადაც დაემატება ციკლის ის რიცხვები, 
რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა"""


sum = 0
for i in range(50, 100 + 1):
    if i % 2 != 0:
        print(i)
    if i > 75:
        sum = sum + i   
        
print(sum)    