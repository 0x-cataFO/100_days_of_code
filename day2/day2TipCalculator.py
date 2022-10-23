# age = input("What is your current age? ")
#
# age_as_int = int(age)
#
# result = 90 - age_as_int
#
#
# days = result * 365
# weeks = result * 52
# months = result * 12
#
# print(f"you have {days} days, {weeks} weeks, and {months} months left.")

print("Welcome to the tip Calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

percent = bill/100 * tip
result = percent + bill

split = int(input("How many people to are split the bill? "))

payment = round(result/split, 2)

print(f"Each person should pay: ${payment}")
