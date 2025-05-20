import turtle
import pandas

#Turn a turtle into a background image:
screen = turtle.Screen()
screen.title("U.S. States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
#-------------------------------------------
#Grabs coordinates of a mouse click and prints it to the console:
#Already there, so you don't need it for this project. ;-)
#Note: Some of the state's x/y coordinates need a little... updating.
# def get_mouse_click_coordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()
#-------------------------------------------
state_data = pandas.read_csv("50_states.csv")
correct_guesses = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(f"Guess A State: {len(correct_guesses)}/50 States Correct",
                                    "What is your guess?").title()
    if answer_state == "Exit":
        #List Comprehension Update:----------------------------
        missed_states = [state for state in state_data.state if state not in correct_guesses]
        #------------------------------------------------------
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")

        # missed_states = []
        # for state in state_data.state:
        #     if state not in correct_guesses:
        #         missed_states.append(state)
        #         new_data = pandas.DataFrame(missed_states)
        #         new_data.to_csv("states_to_learn.csv")
        game_is_on = False

    for state in state_data.state:
        if state == answer_state and answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            correct_answer = state_data[state_data.state == answer_state]
            #Generate a turtle on the map
            answer_turtle = turtle.Turtle()
            answer_turtle.penup()
            answer_turtle.hideturtle()
            answer_turtle.color("black")
            #The .item() method extracts the data, because panda returns an INDEX as well as a value (we only want value)
            answer_turtle.goto(correct_answer.x.item(), correct_answer.y.item())
            answer_turtle.write(f"{correct_answer.state.item()}", align="center", font=("Courier", 8, "normal"))
            if len(correct_guesses) == 50:
                game_is_on = False
                answer_turtle = turtle.Turtle()
                answer_turtle.penup()
                answer_turtle.hideturtle()
                answer_turtle.color("black")
                answer_turtle.goto(0, 0)
                answer_turtle.write("YOU WIN!", align="center", font=("Courier", 24, "normal"))
                screen.exitonclick()
