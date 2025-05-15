from data import question_data

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1 #Increase the question number AFTER it's called, because the list starts at a '0' index
        user_answer = input(f"Q.{self.question_number} - {current_question.text} (True or False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        #Returns a true or false boolean
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong!")
        print(f"Correct Answer: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
