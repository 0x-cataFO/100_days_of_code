row1 = ["😊", "😊", "😊"]
row2 = ["😊", "😊", "😊"]
row3 = ["😊", "😊", "😊"]

table = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# convert the input to index
vertical = int(position[0])
horizontal = int(position[1])
# replace the index
location = table[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")