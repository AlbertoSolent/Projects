import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter number of players between 2 - 4 ")
    if players.isdigit():
        players = int(players)
        if players >=2 and players <=4:
            break
        else:
            print("players must be between 2 -4")
    else:
        print("Invalid input")

max_scores = 50  
player_scores =[ 0 for player in range(players)]


while max(player_scores) < max_scores:

    for player_index in range(players):
        print(f"player {player_index+1}")
        print(f"Your total score is : {player_scores[player_index]}\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)? ").lower()
            if should_roll !="y":
                break
            
            value = roll()
            if value == 1:
                print(f" you rolled 1! Turn done !")
                current_score = 0
                break
            else:
                print(f"you rolled: {value}")
                current_score+=value
            
            print(f"your score is: {current_score}")
        player_scores[player_index]+=current_score
        print(f"Your total score is : {player_scores[player_index]}\n")

max_score = max(player_scores)
win_player_index = player_scores.index(max_score)

print(f"Winner is: {win_player_index+1} with a max score of: {max_score}")

