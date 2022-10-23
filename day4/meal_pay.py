import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names separated by a comma. ")
names = namesAsCSV.split(", ")

length = len(names)

rand = random.randint(0, length)

print(f"{names[rand]} is going to buy the meal today!")
print(names)