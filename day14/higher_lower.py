import art
import game_data
import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def account_data():
    return game_data.data[random.randint(0, 49)]


def follower_count(foll, foll_1, foll_2):
    global account, account_2
    lis = [foll_1, foll_2]
    a = lis[0]
    b = lis[1]
    # foll = followers
    high = max(lis)
    if foll == "a" and a == high:
        return "win"
    elif foll == "b" and b == high:
        return "win"
    else:
        return "Lose"


def feedback(sc, uc):
    global is_game_over, score
    if uc == "win":
        score += 1
    else:
        is_game_over = True


is_game_over = False
score = 0
account = account_data()

while not is_game_over:

    account_2 = account_data()
    if account == account_2:
        account_2 = account_data()

    compare_1 = f"Compare A: {account['name']}, a {account['description']}, from {account['country']}."

    compare_2 = f"Compare B {account_2['name']}, a {account_2['description']}, from {account_2['country']}."

    print(art.logo)

    print(compare_1)
    print(art.vs)
    print(compare_2)

    followers = input("Who has more followers? Type 'A' or 'B': ").lower()

    user_correct = follower_count(foll=followers, foll_1=account['follower_count'], foll_2=account_2['follower_count'])

    scr = feedback(sc=score, uc=user_correct)

    account = account_2
    clear()
    print(f"You're right! Current score : {score}")

if is_game_over:
    clear()
    print(f"Sorry you're wrong. Final score: {score}")

