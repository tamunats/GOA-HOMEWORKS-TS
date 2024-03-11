"""მომხმარებელს შემოატანინე input ფულის რაოდენობა
თუ ეს აღემატება 100 მაშინ დავბეჭდოთ რომ მას გააჩნია საკმარისი 
თანხა. სხვა შემთხვევაში დავბეწდოთ 
რომ მას საკმარისი თანხა არ აქვს"""

deposit_money=int(input("Please deposit money "))

if deposit_money > 100:
    print("you have enough money")
else:
    print("you have not enough money")    