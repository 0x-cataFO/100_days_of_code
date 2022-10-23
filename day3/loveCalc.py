print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Change the names to lower case
name1Lowercase = name1.lower()
name2Lowercase = name2.lower()

# Count number of time "true" appears in name1
tCount1 = name1Lowercase.count("t")
rCount1 = name1Lowercase.count("r")
uCount1 = name1Lowercase.count("u")
eCount1 = name1Lowercase.count("e")
true1 = tCount1 + rCount1 + uCount1 + eCount1

# Count number of time "true" appears in name2
tCount2 = name2Lowercase.count("t")
rCount2 = name2Lowercase.count("r")
uCount2 = name2Lowercase.count("u")
eCount2 = name2Lowercase.count("e")
true2 = tCount2 + rCount2 + uCount2 + eCount2

# Total count1 + count2
trueTotal = true1 + true2

# Count number of time "love" appears in name1
lCount1 = name1Lowercase.count("l")
oCount1 = name1Lowercase.count("o")
vCount1 = name1Lowercase.count("v")
eeCount1 = name1Lowercase.count("e")
love1 = lCount1 + oCount1 + vCount1 + eeCount1

# Count number of time "love" appears in name2
lCount2 = name2Lowercase.count("l")
oCount2 = name2Lowercase.count("o")
vCount2 = name2Lowercase.count("v")
eeCount2 = name2Lowercase.count("e")
love2 = lCount2 + oCount2 + vCount2 + eeCount2

# Total count1 + count2
loveTotal = love1 + love2

# Make a two digit number with to two results
loveScore = trueTotal * 10 + loveTotal

if loveScore < 25 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like a coke and mentos.")
elif loveScore >= 40 and loveScore <= 80:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")



