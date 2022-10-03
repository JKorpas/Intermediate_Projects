from tkinter import *
from quiz_brain import QuizBrain

BACKGROUNDCOLOR = "#B1DDC6"
WORD_FONT = ('Arial', 18, 'bold')


class QuizInterface:
    # After : we can type date type of arg. Helpfull during initialize to pass correct type of arg
    # gives access/visabillity in class while creatin functions. #Type Hints
    def __init__(self, quiz_brain: QuizBrain):
        # "catch" passed quiz_brain
        self.quiz = quiz_brain

        # Main window config
        self.window = Tk()
        self.window.title("Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=BACKGROUNDCOLOR)
        # category Label
        self.category_label = Label(
            text="Category", fg="black", bg=BACKGROUNDCOLOR)
        self.category_label.grid(row=0, column=0)
        # score label
        self.score_label = Label(
            text="Score: 0", fg="black", bg=BACKGROUNDCOLOR)
        self.score_label.grid(row=0, column=1)
        # question canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="Some question", fill="black", font=WORD_FONT, width=285)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        # buttons
        false_button_img = PhotoImage(file="images\\false.png")
        self.false_button = Button(image=false_button_img,
                                   highlightthickness=2, command=self.false_answer)
        self.false_button.grid(row=2, column=0)

        true_button_img = PhotoImage(file="images\\true.png")
        self.true_button = Button(image=true_button_img,
                                  highlightthickness=2, command=self.true_answer)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()
    # example. type data type of passing arg #q_text = self.quiz.next_question()

    def get_next_question(self):
        if self.quiz.still_has_question():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.category_label.config(text=self.quiz.category)
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question_text, text=f"You've completed the quiz, Your final score is {self.quiz.score}/{len(self.quiz.question_list)}")
    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.score_label.config(text=self.quiz.score)
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


