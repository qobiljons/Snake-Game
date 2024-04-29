from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("My Snake Game")
screen.colormode(255)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game = False
        score.game_over()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            score.game_over()

screen.exitonclick()
