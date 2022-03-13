from turtle import Turtle
from random import randint as r_num


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def bonus_food(self):
        """ initializes bonus food"""
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = r_num(-280, 280)
        new_y = r_num(-280, 280)
        self.goto(new_x, new_y)

