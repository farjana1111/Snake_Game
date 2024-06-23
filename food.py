from turtle import Turtle
import random

clr = ["CornflowerBlue", "Purple", "Red", "DeepSkyBlue", "Black", "wheat", "Pink", "SeaGreen","Brown"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.penup()
        self.color(random.choice(clr))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.color(random.choice(clr))
        self.goto(random_x, random_y)
