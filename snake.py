import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0


# Screen configuration
screen = turtle.Screen()
screen.title("Snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Head snake
head = turtle.Turtle()
head.speed(0)
head.color("blue")
head.shape("square")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food snake
food = turtle.Turtle()
food.speed(0)
food.color("purple")
food.shape("circle")
food.penup()
food.goto(0, 110)

# snake body
body = []


# score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0    High Score: 0", align="center",
                 font=("Courier", 24, "normal"))


# funtion to move snake
def up():
    head.direction = "up"


def down():
    head.direction = "down"


def left():
    head.direction = "left"


def right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# keyboard input
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")


while True:
    screen.update()

    # edge collisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # remove body
        for i in body:
            i.goto(2000, 2000)

        body.clear()

        # reset scoreboards
        score = 0
        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score),
                         align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.color("blue")
        new_body.shape("square")
        new_body.penup()
        body.append(new_body)

        # increment score
        score += 10

        if score > high_score:
            high_score = score

        scoreboard.clear()
        scoreboard.write("Score: {}  High Score: {}".format(score, high_score),
                         align="center", font=("Courier", 24, "normal"))
    # append body snake
    bodylen = len(body)
    for i in range(bodylen - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if bodylen > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    # body collisions
    for i in body:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for j in body:
                j.goto(2000, 2000)
            body.clear()

            score = 0
            scoreboard.clear()
            scoreboard.write("Score: {}  High Score: {}".format(score, high_score),
                             align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
