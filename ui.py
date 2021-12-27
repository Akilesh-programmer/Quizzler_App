from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Amazon acquired Twitch in August 2014 for $970 million "
                                                          "dollars",
                                                     fill="black",
                                                     font="Arial 15 italic",
                                                     width=280
                                                     )

        self.right_photo = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_photo, highlightthickness=0, command=self.right_command)
        self.right_button.grid(row=2, column=0)

        self.wrong_photo = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_photo, highlightthickness=0, command=self.wrong_command)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_command(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_command(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



