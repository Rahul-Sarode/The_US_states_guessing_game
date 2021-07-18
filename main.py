import pandas
import turtle

screen = turtle.Screen()

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

data = pandas.read_csv("50_states.csv")
data_state = data.state.to_list()

new_state_list = []
missing_states = []


def score_board():
    for new_state in new_state_list:
        if answer_state == new_state:
            return "state_exist_in_list"


def missing():
    for search_state in data_state:
        if search_state not in new_state_list:
            missing_states.append(search_state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("State_to_learn.csv")
    print(missing_states)


while len(new_state_list) < 50:
    answer_state = screen.textinput(title=f"{len(new_state_list)}/50 State Correct", prompt="What's another state name?").title()
    for i in range(0, 50):
        if answer_state == data_state[i]:
            print(data_state[i])
            if "state_exist_in_list" != score_board():
                new_x = data.x[i]
                new_y = data.y[i]
                tim.write(answer_state)
                new_state_list.append(answer_state)
            print(new_state_list)
    if answer_state == "Exit":
        missing()
        break





