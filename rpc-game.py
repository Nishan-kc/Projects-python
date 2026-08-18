import random

options = ("rock", "paper", "scissor")
is_running = True

while is_running: 
    computer = random.choice(options)
    player = ""
    while player not in options:
        player = input("Enter choice (scissor, paper or rock) : ").strip().lower()

    print(f"your choice: {player}")
    print(f"computer choice : {computer}")

    if player == computer:
        print("Draw")
    elif player == "scissor" and computer == "paper":
        print("Player win")
    elif player == "paper" and computer == "rock":
        print("player win!")
    elif player == "rock" and computer == "scissor":
        print("player win!")
    else:
        print("computer win")

    play_again = input("play again? (y/n): ").strip().lower()
    if play_again != "y":
        is_running = False

print("Thanks for playing !!")
