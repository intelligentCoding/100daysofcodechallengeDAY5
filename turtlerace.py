from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Select the turtle",
                            prompt="Select the which color turtle is going to win? Enter Color: red, orange, yellow, "
                                   "green, blue or purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-238, y=-y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on  = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! {winning_color} color turtle won")
            else:
                print(f"You Lost! {winning_color} color turtle won")

        random_distance = random.randint(0, 15)
        turtle.forward(random_distance)




screen.exitonclick()