def calculate_score(cards):
    if sum(cards) == 21 and sum(cards) == 11+10:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


cds = [10, 10, 11]

print(calculate_score(cds))