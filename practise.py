import random

game = {"r":"🪨",
        "p":"📄",
        "s":"✄"}

choices = ("r", "p", "s")
while True:
    user_choice = input("Enter your choice rock, paper, scissors (r,p,s): ").lower()
    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("invalid choice")
        continue

    print(f"You chose{game[user_choice]}")
    print(f"computer chose {game[computer_choice]}")

    if user_choice == "p" and computer_choice == "r":
        print("you win !")

    elif user_choice == "r" and computer_choice == "s":
        print("you win")

    elif user_choice == "s" and computer_choice == "p":
        print("you win")

    elif user_choice == computer_choice:
        print("its a tie")
    
    else:
        print("computer win")
    
    choice = input("continue: (y/n): ").lower()
    if choice == "n":
        print("Goodbye")
        break
