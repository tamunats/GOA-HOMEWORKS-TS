"""50დან 100 ჩათვლით არსებული 5-ის ჯერადების
 რიცხვთა ჯამი გამოიტანეთ"""

i=50
sum=0

while i <= 100:
    print(i + 5)
    sum=sum + i
    i=i + 5        # ამას იმიტომ ვწერთ რომ უსასრულოდ არ გაგრძელდეს ციკლი
    

print(sum)    