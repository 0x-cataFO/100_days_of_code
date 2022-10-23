import random

print("Welcome to  Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")


def number():
    return random.randint(1, 100)


number = number()


def easy():
    # global number
    is_correct = False
    chance = 11
    while not is_correct:
        chance -= 1
        print(f"You have {chance} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if chance == 1:
            print("You've run out of guesses you lose!")
            is_correct = True
        elif guess > number:
            print("Too high. \nGuess again.")
        elif guess < number:
            print("Too low. \nGuess again.")
        elif guess == number:
            print(f"You got it! The answer is {guess}")
            is_correct = True


def hard():
    # global number
    is_correct = False
    chance = 6
    while not is_correct:
        chance -= 1
        print(f"You have {chance} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if chance == 1:
            print("You've run out of guesses, you lose!")
            is_correct = True
        elif guess > number:
            print("Too high. \nGuess again.")
        elif guess < number:
            print("Too low. \nGuess again.")
        elif guess == number:
            print(f"You got it! The answer is {guess}")
            is_correct = True


correct_syntax = False

while not correct_syntax:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        correct_syntax = True
        easy()
    elif difficulty == "hard":
        correct_syntax = True
        hard()
    else:
        print("Invalid input, Try again.")
easy