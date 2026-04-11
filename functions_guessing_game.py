from random import *

def get_random_number():
    random_num = randint(1, 10)
    return random_num

def user_guess():
    guess = int(input("Enter a number: "))
    return guess

def check_guess(number, guess):
    if number == guess:
        return True
    else:
        return False
    



def play_game():
    while True:  # Outer loop: play multiple rounds
        number = get_random_number()
        attempts = 0

        while True:  # Inner loop: keep guessing until correct
            guess = user_guess()
            attempts += 1

            if check_guess(number, guess):
                print(f"Correct! You guessed it in {attempts} tries 🎉")
                break
            else:
                if guess > number:
                    print("Too high!")
                else:
                    print("Too low!")

        user_choice = input("Do you want to play again? y/n ").lower()
        if user_choice == "n":
            break


play_game()
