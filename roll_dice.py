import random

while True:
    user_choice = input("roll dice: y/n ").lower()
    if user_choice == "y":
        how_many = int(input("how many dices do u wanna roll: "))
        rolls = []
        
        for i in range(how_many):
            dice = random.randint(1, 6)
            rolls.append(dice)
        print(rolls)

    elif user_choice == "n":
        break

    else:
        print("invalid choice")