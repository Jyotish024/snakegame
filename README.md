import time

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()
screen.exitonclick()

