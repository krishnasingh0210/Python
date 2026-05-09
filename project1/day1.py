#1 Print Hello world
print ("Hello world!")

#2 Print the sum of 1 and 2
print (1 + 2)       

#3 Print the result of 1 + 2, then multiply by 3
print ((1 + 2) * 3) 

#4 Print the result of 1 + 2, then multiply by 3, then divide by 4
print (((1 + 2) * 3) / 4)

#5 Quiz Program
import random

# list of questions (Question, Options, Answer)
quiz_questions = [
    {
        "question": "What is the output? print(type([]))",
        "options": ["A) list", "B) tuple", "C) dict", "D) set"],
        "answer": "A"
    }, 
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "What is the output? print(2 ** 3)",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    },
    {
        "question": "What will this code output? a=[1,2,3]; b=a; b.append(4); print(a)",
        "options": ["A) [1,2,3]", "B) [1,2,3,4]", "C) Error", "D) None"],
        "answer": "B"
    },
    {
        "question": "What does len('Hello') return?",
        "options": ["A) 4", "B) 5", "C) 6", "D) Error"],
        "answer": "B"
    },
    {
        "question": "What is the output? print(bool(0))",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Which is used to handle exceptions?",
        "options": ["A) try-except", "B) if-else", "C) loop", "D) function"],
        "answer": "A"
    },
    {
        "question": "What is the output? x='Python'; print(x[::-1])",
        "options": ["A) Python", "B) nohtyP", "C) Error", "D) None"],
        "answer": "B"
    },
    {
        "question": "What will this print? for i in range(3): print(i)",
        "options": ["A) 1 2 3", "B) 0 1 2", "C) 0 1 2 3", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Correct way to create a dictionary?",
        "options": ["A) {1,2,3}", "B) [1:2,2:3]", "C) {1:2,2:3}", "D) (1:2,2:3)"],
        "answer": "C"
    },
    {
        "question": "What is the output? print('5' + '5')",
        "options": ["A) 10", "B) 55", "C) Error", "D) 5"],
        "answer": "B"
    },
    {
        "question": "What is the output? print(10/3)",
        "options": ["A) 3", "B) 3.33", "C) 3.333333...", "D) Error"],
        "answer": "C"
    },
    {
        "question": " What happens here? a = (1, 2, 3) , a[0]=5",
        "options": ["A) (5, 2, 3)", "B) Error", "C) True", "D) None"],
        "answer": "B"
    },
    {
        "question": " What will this output? print(bool('False')) ",
        "options": ["A) False", "B) True", "C) Error ", "D) None"],
        "answer": "B"
    },
    {
        "question": " What will this output? x = [1, 2, 3]   print(x[3])",
        "options": ["A) 3", "B) 0", "C) Error ", "D) None"],
        "answer": "C"
    }
]

def run_quiz():
    # This Function is to control the quiz game
    score = 0
    total = len(quiz_questions)

    print(" Welcome to Python Quiz Game!\n")
    name = str(input("Enter Player name : "))
    random.shuffle(quiz_questions)      #shuffle is a keyword used to shuffle the questions everytime when program starts .

    for i, q in enumerate(quiz_questions, 1): #handler comes first in enumerate
        print(f"\nQuestion {i}: {q['question']}") #quiz_questions comes q where as 1 comes in i
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(" Correct Answer !!")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}")

    percentage = (score / total) * 100

    print("\n Quiz Completed!," , name)
    print(name, f",Your Score is: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print(" you are Excellent!", name)
    elif percentage >= 50:
        print("Good job!", name)
    else:
        print(" Keep practicing!", name)

# Run the quiz
run_quiz()

#6 Print the current date and time
from datetime import datetime
current_datetime = datetime.now()
print("Current date and time:", current_datetime)   

#7 Print the first 10 Fibonacci numbers
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print("First 10 Fibonacci numbers:", fibonacci(10))

#8 Print the factorial of 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

