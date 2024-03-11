"""4) მომხმარებელს შემოატანინეთ აჯიმანიებისა და ბუქნების რაოდენობა,
 ტქვენ კი შეამოწმეთ უდრის თუ არა აჯიმანიების რაოდენობა აუცილებელს
 ან ბუქნების რაოდენობა აუცილებელს"""


required_pushups=70
required_squads=40

pushups=int(input("How many pushups have you done? "))
squads=int(input("How many squads have you done? "))

print(required_pushups <= pushups or required_squads <= squads)