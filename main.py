from snake import Snake
from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

cobra = Snake()
food = Food()   
scoreboard = ScoreBoard()

screen.update()
screen.listen()
screen.onkey(key="Up", fun=cobra.up)
screen.onkey(key="Down", fun=cobra.down)
screen.onkey(key="Right", fun=cobra.right)
screen.onkey(key="Left", fun=cobra.left)
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    cobra.move()
    # detect collision with food
    if cobra.head.distance(food) < 15:
        food.refresh()
        cobra.extend()
        scoreboard.score_change()
    # detect collision with wall
    if cobra.head.xcor() > 280 or cobra.head.xcor() < -300 or cobra.head.ycor() > 280 or cobra.head.ycor() < -280:

        scoreboard.reset()
        cobra.reset()
    # detect collision with tail

    for segment in cobra.segments[1::]:



        if cobra.head.distance(segment) < 10:
            cobra.reset()
            scoreboard.reset()
 

screen.exitonclick()
