import turtle

wn = turtle.Screen()
wn.title("Pong by @Abai Raj.K")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score

score_a = 0
score_b = 0

# first paddle

first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape("square")
first_paddle.color("red")
first_paddle.shapesize(stretch_wid=7, stretch_len=1)
first_paddle.penup()
first_paddle.goto(-350, 0)

# second paddle

second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape("square")
second_paddle.color("red")
second_paddle.shapesize(stretch_wid=7, stretch_len=1)
second_paddle.penup()
second_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("pink")
ball.penup()
ball.goto(0, 0)
#  ball movement
ball.dx = 0.2
ball.dy = -0.2

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 18, "normal"))


# functions

# paddle 1
def first_paddle_up():
    y = first_paddle.ycor()
    y += 20
    first_paddle.sety(y)


def first_paddle_down():
    y = first_paddle.ycor()
    y -= 20
    first_paddle.sety(y)


# paddle 2
def second_paddle_up():
    y = second_paddle.ycor()
    y += 20
    second_paddle.sety(y)


def second_paddle_down():
    y = second_paddle.ycor()
    y -= 20
    second_paddle.sety(y)


def quit_():
    wn.clear()
    pen.goto(0, 0)
    pen.write("PONG", align="center", font=("Courier", 18, "normal"))


# keyboard binding

wn.listen()
wn.onkeypress(first_paddle_up, "w")
wn.onkeypress(first_paddle_down, "s")
wn.onkeypress(second_paddle_up, "Up")
wn.onkeypress(second_paddle_down, "Down")

# Main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #  Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player 1: {score_a}  Player 2: {score_b}", align="center", font=("Courier", 18, "normal"))

    # paddle and ball collisions
    if 340 < ball.xcor() < 350 and (second_paddle.ycor() + 50 > ball.ycor() > second_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and (first_paddle.ycor() + 50 > ball.ycor() > first_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    wn.onkeypress(quit_, "q")

