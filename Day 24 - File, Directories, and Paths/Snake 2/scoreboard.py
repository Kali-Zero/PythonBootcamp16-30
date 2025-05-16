from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0 #Leaving this here in case the file gets wiped
        with open("data.txt", mode="r") as file:
            self.highscore = file.read()
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"High Score: {self.highscore} | Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
