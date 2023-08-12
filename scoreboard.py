from turtle import Turtle
ALIGNMENT = 'center'
FONT =('Courier', 20, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_change(self):
        self.score += 1
        self.score_update()

    def reset(self) :
        self.clear()
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
        self.score_update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER ", move=False, align=ALIGNMENT, font=FONT)

