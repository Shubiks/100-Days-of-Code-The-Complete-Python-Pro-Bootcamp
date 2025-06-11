from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.scoreboard = Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.scoreboard.grid(row=0,column=1)

        self.questionboard = Canvas(width=300,height=250,bg="white")
        self.question_text = self.questionboard.create_text(150, 125,text="Question Text", width=280, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.questionboard.grid(row=1,column=0,columnspan=2,pady=50)

        

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.questionboard.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.questionboard.itemconfig(self.question_text, text=q_text)
        else:
            self.questionboard.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.scoreboard.config(text=f"Final Score: {self.quiz.score}")
        

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.questionboard.config(bg="green")
        else:
            self.questionboard.config(bg="red")
        self.window.after(1000,self.get_next_question)
        
        