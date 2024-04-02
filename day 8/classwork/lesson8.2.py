target_pushups = 100
target_squads = 50

pushups = int(input("How many pushups have you done: "))
squads = int(input("How many squads have you done: "))

print(pushups == target_pushups or squads == target_squads)
print(pushups >= target_pushups or squads >= target_squads)

