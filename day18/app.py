import random
import turtle as t

timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = r, g, b
    return tup


i = 0
# timmy.width(2)
angle = [0, 90.0, 180.0, 270.0]

while i < 360:
    timmy.color(random_color())
    timmy.circle(60)
    # timmy.forward(30)6
    timmy.seth(i)
    i += 4

screen.screensize(100, 100, 'orange')
screen.exitonclick()
