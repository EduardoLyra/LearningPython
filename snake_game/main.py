from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')

    game_is_on = True

    while game_is_on:
        screen.update()
        sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            score.add_score()
            snake.extends()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
    screen.exitonclick()


if __name__ == '__main__':
    main()
