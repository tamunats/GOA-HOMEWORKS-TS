"""3) შექმენით 2 ცვლადი სადაც შეტანილი გექნებათ ადამიანის წონა და სიმაღლე, 
(required_weight,required_height) რომლის მნიშვნელობაც იქნება 50 და 170 , შემდეგ
მომხმარებელს შემოატანინეთ მისი წონა input ფუნქციის მეშვეობით
და შეამოწმეთ მომხმარებლის წონა თუ უდრის required_weight ცვლადს
და მომხარებლის სიმაღლე თუ უდრის required_height, აგრეთვე
მეორე პრინტში შეამოწმეთ თუ აღემატება წონას და ნაკლებია სიმაღლეზე, 
თითქმის ყველა კომბინაცია შედარების ოპერატორების."""




required_weight = 50
required_hight = 170

weight=int(input("your weight: "))
hight=int(input("your hight: "))

print(required_weight == weight and required_hight == hight)
print(required_weight < weight and required_hight > hight )
print(required_weight <= weight and required_hight >= hight )
print(required_weight < weight and required_hight >= hight )
print(required_weight <= weight and required_hight > hight )
print(required_weight > weight and required_hight < hight )
print(required_weight != weight and required_hight != hight )


print(required_weight == weight or required_hight == hight)
print(required_weight < weight or required_hight > hight )
print(required_weight <= weight or required_hight >= hight )
print(required_weight < weight or required_hight >= hight )
print(required_weight <= weight or required_hight > hight )
print(required_weight > weight or required_hight < hight )
print(required_weight != weight or required_hight != hight )

print(not(required_weight == weight and required_hight == hight))
print(not(required_weight < weight and required_hight > hight ))
print(not(required_weight <= weight and required_hight >= hight ))
print(not(required_weight < weight and required_hight >= hight ))
print(not(required_weight <= weight and required_hight > hight ))
print(not(required_weight > weight and required_hight < hight ))
print(not(required_weight != weight and required_hight != hight ))

