import random
from turtle import Turtle, Screen
colours = ["red","blue","purple", "orange"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet:", prompt="Which turtle will win the race? red, blue , purple or "
                                                            "orange").lower()
colors_num = 0
y = -150
bet_on = False
turtles = ["tim", "john", "apple", "poppy"]
tort_object = []
for tort in turtles:
    tort = Turtle()
    tort.shape("turtle")
    tort.color(colours[colors_num])
    colors_num += 1
    tort.penup()
    tort.goto(-230, y)
    y += 50
    tort_object.append(tort)

if user_bet:
    bet_on = True

while bet_on:
    for turtle in tort_object:
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)
        if turtle.xcor() >= 223.0:
            bet_on = False
            colour = turtle.pencolor()
            if user_bet == colour:
                print(f"Congratulations! You Win. The Winning Turtle was {colour}.")
            else:
                print(f"Sorry! You Lost. The Winning turtle was {colour}.")















screen.exitonclick()

