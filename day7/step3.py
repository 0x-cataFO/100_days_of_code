import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Psst, the solution is {chosen_word}")

# Create Blanks
display = []
for letter in range(len(chosen_word)):
    display += "_"

# TODO-1: - Use  while loop to let the user guess again. The loop should stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for blank in range(len(chosen_word)):
        letter = chosen_word[blank]
        # print(f"Current position: {blank}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[blank] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")
