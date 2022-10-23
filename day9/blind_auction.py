from art import logo
import os

def highest_bid(bidding_record):
    highest_amount = 0
    winner = ""
    for bidder in auction:
        bid_amount = auction[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_amount}.")


def add_new_bidder(bidder_name, bidder_bid):
    auction[bidder_name] = bidder_bid


auction = {}

print(logo)
print("Welcome to the Secret auction program")

new_bidder = True
while new_bidder:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_new_bidder(bidder_name=name, bidder_bid=bid)

    cont = input("Are there any other bidders? type 'yes' or 'no'.\n")
    if cont == "yes":
        new_bidder = True
        os.system('cls')
    elif cont == "no":
        new_bidder = False
        highest_bid(bidding_record=auction)
