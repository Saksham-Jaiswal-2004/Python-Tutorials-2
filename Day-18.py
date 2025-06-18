import random
import turtle
from turtle import Turtle
from turtle import Screen as sC # Aliasing Modules

timmy = Turtle()
screen = sC()
turtle.colormode(255)

timmy.shape("turtle")
timmy.color("white")

screen.bgcolor("black")

# for i in range(4):
#     for j in range(5):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#     timmy.right(90)

colors = [
    "medium violet red", "dodger blue", "lime green", "gold", "orchid",
    "coral", "slate blue", "turquoise", "firebrick", "dark orange"
]
# timmy.pensize(10)
# timmy.speed("fast")
#
# for i in range (5):
#     timmy.color(random.choice(colors))
#     for j in range (3+i):
#         for k in range(5):
#             timmy.forward(20)
#             timmy.color(random.choice(colors))
#         timmy.left(360/(i+3))

# directions = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fast")

# for i in range (200):
#     timmy.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

timmy.speed("fastest")
gap = 5
for i in range(int(360/gap)):
    timmy.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.circle(100)
    timmy.left(gap)

screen.exitonclick()