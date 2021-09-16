from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(False)

snake = Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        curr_scr=food.current_score()
        score.write_score(curr_scr)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor () <-280:
        score.game_over()
        game_is_on=False

    for i in snake.turtle_list[1:]:
        if snake.head.distance(i)<10:
            score.game_over()
            game_is_on=False



screen.exitonclick()