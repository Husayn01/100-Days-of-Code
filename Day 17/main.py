from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(0, len(question_data) - 1):
    question_text = question_data[i]["text"]
    question_answer = question_data[i]["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")