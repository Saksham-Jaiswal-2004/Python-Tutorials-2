import turtle, pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guessed Correct", "What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
        guessed_states.append(answer_state)

screen.exitonclick()