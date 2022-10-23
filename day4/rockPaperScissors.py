import random

rock = '''
    rock
'''

paper = '''
    paper
'''

scissors = '''
    scissors
'''

objects = [rock, paper, scissors]

rand = random.randint(0, 2)

# option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# my_choice = objects[option]
# computer_choice = objects[rand]

my_choice = objects[0]
computer_choice = objects[2]

print(my_choice)
print("Computer chose:")
print(computer_choice)

if my_choice < computer_choice:
    print("You Lose")
elif my_choice == 0 and computer_choice == 2:
    print("You win!")
elif my_choice == computer_choice:
    print("Draw")
else:
    print("You win!")

