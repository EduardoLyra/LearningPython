from random import choices, randint
from turtle import Turtle, xcor


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        new_car = Turtle('square')
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.color(choices(COLORS))
        y_cor = randint(0, 260)
        signal = randint(0, 1)
        new_car.penup()
        if signal == 1:
            y_cor *= -1
        new_car.goto(280, y_cor)
        self.cars.append(new_car)
        self.move(y_cor)

    def move(self, y_cor):
        for i in range(len(self.cars)):
            self.cars[i].goto(-280, y_cor)
