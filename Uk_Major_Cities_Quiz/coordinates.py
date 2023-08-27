from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=550, height=750)
screen.bgpic('uk_map.png')
screen.title('Snake Game')
tim.penup()


def forward():
    tim.forward(5)


def backward():
    tim.backward(5)


def left():
    tim.left(10)


def right():
    tim.right(10)


def get_coord():
    with open('uk_cities.csv', 'a') as files:
        files.write(str(tim.xcor()) + ', ' + str(tim.ycor())+'\n')


screen.listen()
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(get_coord, 'g')
screen.onkey(tim.pendown, 'r')
screen.onkey(tim.penup, 'q')

screen.exitonclick()