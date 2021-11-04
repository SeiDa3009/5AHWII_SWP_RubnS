import random
import sys

values = ["Rock", "Paper", "Scissors"]
repeat = True
user_score = 0
ki_score = 0
tie_score = 0

while (repeat):
    try:
        user_choice = int(input("Rock [0], Paper [1] or Scissors [2]: "))
        user_choice_value = values[user_choice]
    except (ValueError, KeyError, Exception):
        print(user_choice_value)
        print("Lose by default ... no correct input")
        sys.exit(0)

    ki_choice = random.randint(0, 2)
    ki_choice_value = values[ki_choice]

    print("User: " + user_choice_value)
    print("KI: " + ki_choice_value)

    # check who wins
    if ki_choice == user_choice:
        print("Tie!")
        tie_score += 1
    elif (user_choice + 1) % 3 == ki_choice:
        print("You lose!")
        ki_score += 1
    else:
        print("You win!")
        user_score += 1

    repeat_input = input("Play again? [Y/N]: ")
    if repeat_input.upper() == "Y":
        repeat = True
    else:
        repeat = False

games = user_score + ki_score;
print("Scorings: ")
print("%s Wins" %user_score)
print("%s Losses" %ki_score)
print("%s Ties" %tie_score)


