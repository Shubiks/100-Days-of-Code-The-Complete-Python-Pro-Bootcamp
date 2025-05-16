class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        self.question_number+=1
        ans = str(input(f"Q{self.question_number}: {self.question_list[self.question_number-1].q}Type True/False: ")).title()
        self.check_ans(ans,self.question_list[self.question_number-1].ans)

    def still_has_question(self):
        return not self.question_number == len(self.question_list)

    def check_ans(self,user_ans,correct_ans):
        if user_ans == correct_ans:
            print("You got it right")
            self.score +=1
        else:
            print("That's wrong")
        print(f"The Correct Answer was : {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
