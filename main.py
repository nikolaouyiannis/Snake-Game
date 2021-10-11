from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initiate our game's screen
screen = Screen()
# Use keyword arguments to help whoever reads the code 
screen.setup(width=600, height=600)
# Background color
screen.bgcolor("black")
# Title of game
screen.title("My Snake Game")
# Turning of tracer
screen.tracer(0)

# Create Snake
snake = Snake()
# Create food
food = Food()
# Create Scoreboard
scoreboard = Scoreboard()


# Start listening for key strokes
screen.listen()
# Listen for these key strokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:

    # Updates screen after each iteration is complete, so the snake seems to move as a whole
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    
















screen.exitonclick()