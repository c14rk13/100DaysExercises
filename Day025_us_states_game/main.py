import turtle
import pandas


image_path = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image_path)
turtle.shape(image_path)

state = turtle.Turtle()
state.hideturtle()
state.penup()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
correct_guesses = []

game_on = True
while len(correct_guesses) < 50:
    # Ask the user for a state's name; Capitalize the state name
    answer_state = screen.textinput(f"{len(correct_guesses)}/50 States Correct", "What's another State's name?").title()

    if answer_state == "Exit":
        missing_guesses = [state for state in all_states if state not in correct_guesses]
        # OR:
        # missing_guesses = list(set(all_states) - set(correct_guesses))
        data_states_to_learn = pandas.DataFrame(missing_guesses)
        data_states_to_learn.to_csv("states_to_learn.csv")
        break

    data_state = data[data.state == answer_state]
    if not data_state.empty:
        x = int(data_state.x.item()) # OR, instead of item(), use iloc[0]
        y = int(data_state.y.item())
        state.goto(x, y)
        state.write(answer_state, align="center")
        correct_guesses.append(data_state.state.item())




