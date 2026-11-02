import random

choices = ["rock", "paper", "scissors"]

comp = 0
play = 0

while True:
    computer = random.choice(choices)

    player = input("Choose between rock, paper, scissors: ").lower()

    if player not in choices:
        print("Please choose a valid answer!")
        continue

    print("You chose:", player)
    print("Computer:", computer)

    if computer == player:
        print("It's a draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("You win!!")
        play += 1

    else:
        print("Computer wins!!")
        comp += 1

    print("Player:", play)
    print("Computer:", comp)