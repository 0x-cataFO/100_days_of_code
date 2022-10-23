import turtle as t

tut = t.Turtle()
screen = t.Screen()


def move_forward():
    tut.forward(10)


def move_backward():
    tut.backward(10)


def clockwise():
    tut.seth(tut.heading() + 10)


def counter_clockwise():
    tut.seth(tut.heading() - 10)


screen.listen()
screen.onkey(key="W".lower(), fun=move_forward)
screen.onkey(key="S".lower(), fun=move_backward)
screen.onkey(key="D".lower(), fun=clockwise)
screen.onkey(key="A".lower(), fun=counter_clockwise)
screen.onkey(key="C".lower(), fun=tut.reset)
screen.exitonclick()
