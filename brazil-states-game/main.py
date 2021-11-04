import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=725)
screen.title("Brazil States Game")
image = "brazil-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('brazil-states-game/27-states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 27:
    user_guess = screen.textinput(
        f'{len(guessed_states)}/27 States Correct', "What's another state name? (without special caracters)").upper()
    if user_guess == 'EXIT':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if user_guess in all_states:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.abrev.item(), font=('Arial', 8, 'bold'))
