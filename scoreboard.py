from turtle import Turtle,Screen
# screen = Screen()
# screen.bgcolor("black")
# SCORE = 0
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 278)
        self.write(f"score is:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """moves score board to top and displays score"""
        self.goto(0, 0)
        self.clear()
        self.write(f"Game Over!! ◔_◔ \nscore is:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        """ updates score"""
        self.clear()
        self.score += 5
        self.write(f"score is:{''}{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_bonusscore(self):
        """updates special bonus score"""
        self.clear()
        self.score += 20
        self.write(f"score is:{''}{self.score}", move=False, align=ALIGNMENT, font=FONT)





# score = Score()
#
# screen.exitonclick()