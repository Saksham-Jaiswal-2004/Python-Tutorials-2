import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
user_bet = screen.textinput("Make Your Bet", "Which Turtle will win the race? Enter a color:" )
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range (0,6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(-230, -200+(80*i))
    tim.color(colors[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if(turtle.pencolor() == user_bet):
                print(f"You've Won! The {turtle.pencolor()} turtle is the winner.")
            else:
                print(f"You've Lost! The {turtle.pencolor()} turtle is the winner.")

            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward((rand_distance))

screen.exitonclick()