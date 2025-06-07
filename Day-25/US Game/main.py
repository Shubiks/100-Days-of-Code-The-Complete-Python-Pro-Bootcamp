import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    user_input = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="Type the State name").title()

    state_data = pd.read_csv("50_states.csv")
    states = state_data.state.to_list()

    if user_input == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_state = pd.DataFrame(missing_states)
        new_state.to_csv("missing_states.csv")
        break
        

    for state in states:
        if state == user_input:
            turt = turtle.Turtle()
            turt.hideturtle()
            turt.penup()
            state_info = state_data[state_data.state == state]
            guessed_states.append(state)
            turt.goto(state_info.x.item(),state_info.y.item())
            turt.write(user_input)




















screen.mainloop()