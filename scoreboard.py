from turtle import Turtle




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score {self.score}", align="center", font=("Arial", 20, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Arial",20,"normal"))
