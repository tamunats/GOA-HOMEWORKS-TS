target_pushups = 100
target_squads = 50

pushups = int(input("How mane pushups have you done: "))
squats = int(input("How mane squads have you done: "))

print(pushups == target_pushups or squats == target_squads)
print(pushups >= target_pushups or squats >= target_squads)