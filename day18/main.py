import turtle as t
import random
color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]

tut = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tut.speed("fastest")

tut.hideturtle()
tut.pu()
tut.right(90)
tut.forward(200)
tut.right(90)
tut.forward(210)
tut.seth(0)

i = 0

while i < 10:
    for num in range(1, 11):
        tut.dot(20, random.choice(color_list))
        tut.forward(50)

    tut.left(90)
    tut.forward(50)
    tut.left(90)
    tut.forward(500)
    tut.seth(0)
    i += 1

# for i in range(1, 10):
#     tut.color(random.choice(color_list))
#     tut.begin_fill()
#     tut.circle(5)
#     tut.penup()
#     tut.forward(50)
#     tut.pendown()
#     tut.circle(5)
#     tut.end_fill()



# screen.screensize(100, 100, 'orange')
# screen.window_height()
# screen.window_width()
screen.exitonclick()
