from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}", font=FONT)
    def increase_score(self):
        self.level += 1
        self.update_score()
    def gameover(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)