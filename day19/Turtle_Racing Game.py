import random
import turtle as t

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
position = [-70, -40, -10, 20, 50, 80]
all_tuts = []

for tut_pos in range(0, 6):
    tut = t.Turtle(shape="turtle")
    tut.color(colors[tut_pos])
    tut.penup()
    tut.goto(x=-230, y=position[tut_pos])
    all_tuts.append(tut)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_tuts:
        if turtle.xcor() > 230:
            winning_tut = turtle.pencolor()
            if user_bet == winning_tut:
                print(f"You've won! The {winning_tut} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_tut} turtle is the winner!")
            is_race_on = False


        rand_num = random.randint(0, 10)
        turtle.forward(rand_num)
# orange = t.Turtle(shape="turtle")
# orange.penup()
# orange.goto(x=-230, y=-70)
#
# yellow = t.Turtle(shape="turtle")
# yellow.penup()
# yellow.goto(x=-230, y=-40)
#
# green = t.Turtle(shape="turtle")
# green.penup()
# green.goto(x=-230, y=-10)
#
# blue = t.Turtle(shape="turtle")
# blue.penup()
# blue.goto(x=-230, y=20)
#
# purple = t.Turtle(shape="turtle")
# purple.penup()
# purple.goto(x=-230, y=50)


screen.exitonclick()
