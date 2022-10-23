import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

my_choice = int(input("What do you choose? 0 for Rock, 1 Paper or 2 for Scissors.\n"))

if my_choice == 0:
    print("Rock")
elif my_choice == 1:
    print("Paper")
elif my_choice == 2:
    print("Scissors")

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print("Computer chose:\nRock")
    elif computer_choice == 1:
        print("Computer chose:\nPaper")
    elif computer_choice == 2:
        print("Computer chose:\nScissors")

    if my_choice == computer_choice:
        print("Draw")
    elif my_choice < computer_choice:
        print("You Lose")
    else:
        print("You Win")
else:
    print("Invalid choice")

