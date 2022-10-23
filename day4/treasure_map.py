
'''
This is a program which will mark a spot X
The map is made up of 3 rows of blank squares
'''

row1 = ['😒', '😂', '😎']
row2 = ['😒', '😂', '😎']
row3 = ['😒', '😂', '😎']

mape = [row1, row2, row3]

'''
This program allows you to enter a position of the treasure
using a two digit system. The first digit is the horizontal
column number and the second digit is the vertical column number
'''

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")

column = int(position[0]) - 1
row = int(position[1]) - 1

mape[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}")
