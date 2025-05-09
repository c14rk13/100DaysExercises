from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")
SCORE_HOME_X = 0
SCORE_HOME_Y = 270

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        # Write initial score on screen
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.goto(SCORE_HOME_X, SCORE_HOME_Y)
        self.high_score = self.read_high_score()
        self.write_score()


    def update_score(self):
        self.score += 1
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, align=ALIGNMENT,
                   font=FONT)


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.write_score()


    def read_high_score(self):
        with open("data.txt") as score_file:
            return int(score_file.read())


    def write_high_score(self):
        with open("data.txt", mode="w") as score_file:
            score_file.write(f"{self.high_score}")


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, align=ALIGNMENT,
    #                font=FONT)