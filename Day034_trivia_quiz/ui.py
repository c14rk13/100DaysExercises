from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
IMG_TRUE = "./images/true.png"
IMG_FALSE = "./images/false.png"
FONT_NAME = "Arial"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", font=(FONT_NAME, 10, "normal"), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.text_quiz_question = self.canvas.create_text(150,125,
                                                          width=280,
                                                          text="Quiz question here",
                                                          fill=THEME_COLOR,
                                                          font=(FONT_NAME, 15, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        image_true = PhotoImage(file=IMG_TRUE)
        image_false = PhotoImage(file=IMG_FALSE)

        self.btn_true = Button(image=image_true, highlightthickness=0,
                               bg=THEME_COLOR, bd=0,
                               command= lambda: self.check_answer("true"))
        self.btn_true.grid(column=0, row=2, padx=20)

        self.btn_false = Button(image=image_false, highlightthickness=0,
                                bg=THEME_COLOR, bd=0,
                               command= lambda: self.check_answer("false"))
        self.btn_false.grid(column=1, row=2, padx=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_quiz_question, text=q_text)
        else:
            msg_txt = (f"You've completed the quiz"
            f"\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.canvas.itemconfig(self.text_quiz_question, text=msg_txt)
            self.btn_false.config(state=DISABLED)
            self.btn_true.config(state=DISABLED)


    def check_answer(self, answer):
        is_correct = self.quiz.check_answer(answer)
        self.score.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_correct)


    def give_feedback(self,is_correct):
        if is_correct: # briefly flash green background
            self.canvas.config(bg="green")
        else: # briefly flash red background
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)


