import turtle
import pandas

screen = turtle.Screen()
screen.title("State Guessing Game")
image = "political-map_img.gif"
screen.bgpic(image)
turtle.ht()

guess = []
while len(guess) < 50:
    states = screen.textinput(title=f"{len(guess)}/28 correct state", prompt="What's another state name?").title()
    content = pandas.read_csv("india_states.csv")
    content_state = content.state.to_list()
    if states == "Exit":
        missing = [state for state in content_state if state not in guess]
        missing_count = len(missing)
        screen.clear()
        screen.textinput(title="WOW!", prompt=f"The missing states are {missing_count}. They are {missing}")
        break
    if states in content_state:
        guess.append(states)
        tom = turtle.Turtle()
        tom.ht()
        tom.pu()
        state_position = content[content.state == states]
        tom.goto(float(state_position.x), float(state_position.y))
        tom.write(state_position.state.item())


