class QuizBrain():
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_questions(self):
        if self.question_number != len(self.question_list):
            return True
        else:
            return False





    def next_question(self):

        self.question = self.question_list[self.question_number].text
        self.crt_answer = self.question_list[self.question_number].answer
        self.user_answer = input(f"Q.{self.question_number+1} : {self.question} (True/False): ").lower()
        self.question_number += 1
        self.check_answer(self.user_answer,self.crt_answer)
        # if self.user_answer == self.crt_answer:
        #     print(f"You got it right!")
        #     self.score += 1
        # else:
        #     print("That's wrong!")
        # print(f"The correct answer was :{self.crt_answer}")
        #self.current_score = f"{self.score} / {self.question_number}T"
        # print(f"Your current score is : {self.current_score}")
    def check_answer(self,user_answer,crt_answer):
        if self.user_answer == self.crt_answer.lower():
            print(f"You got it right!")
            self.score+=1
        else:
            print(f"That's wrong")
        print(f"The correct answer was: {self.crt_answer}")
        self.current_score = f"{self.score} / {self.question_number}"
        print(f"You current score is: {self.current_score}")
        print("\n")