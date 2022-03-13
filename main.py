from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0) # turns off the animation
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  # refreshes and redraws screen
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.update_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # detecting wall collisions
        score.game_over()
        game_is_on = False
    # detect any collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
screen.exitonclick()
