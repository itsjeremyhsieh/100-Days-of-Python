THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=50, pady=20)
        self.score_label = Label(text="Score: 0", fg="white")
        self.score_label.config(bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canva = Canvas(width=300, height=250, bg="white")
        self.question = self.canva.create_text(150, 125, text="Question here!", font=("Ariel", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canva.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_img = PhotoImage(file="./images/true.png")
        self.right = Button(image=self.right_img, highlightthickness=0, command=self.click_right)
        self.right.grid(row=2, column=0)
        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=self.wrong_img, highlightthickness=0, command=self.click_wrong)
        self.wrong.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question, text=q_text)
        else:
            self.canva.itemconfig(self.question, text="This is the end of the test!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def click_right(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def click_wrong(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canva.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.get_next_question)
