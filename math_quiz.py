"""A simple math quiz game with four basic operations, time limit, and scoring system."""

import random
import time

operations = ["*", "/", "+", "-"]
TIMES = 0
SCORES = 0
TIME_LIMIT = 10
while TIMES < 5:
    operation = random.choice(operations)
    if operation == "*":
        first_number = random.randint(-15, 15)
        second_number = random.randint(-15, 15)
        correct_answer = first_number * second_number
    elif operation == "/":
        first_number = random.randint(-10, 10)
        second_number = random.randint(-10, 10)
        if second_number == 0:
            while second_number == 0:
                second_number = random.randint(-10, 10)
        correct_answer = int(first_number / second_number)
    elif operation == "+":
        first_number = random.randint(-99, 99)
        second_number = random.randint(-99, 99)
        correct_answer = first_number + second_number
    else:
        first_number = random.randint(-99, 99)
        second_number = random.randint(-99, 99)
        correct_answer = first_number - second_number

    start_time = time.time()
    print(f"Question {TIMES + 1}")
    if operation == "/":
        print("Note: In division, the answer is the correct expression!")
    try:
        user_answer = int(input(f"{first_number} {operation} {second_number} ?\n"))
    except ValueError:
        print("Please enter a valid number!")
        continue
    end_time = time.time()

    if end_time - start_time <= TIME_LIMIT:
        if user_answer == correct_answer:
            SCORES += 1
            print(f"That's right. SCORES: {SCORES}")
        else:
            print(f"That's wrong. SCORES: {SCORES}")
    else:
        print(f"Your time is finished. SCORES: {SCORES}")
    TIMES += 1

print(f"\nEnd Game!\nYou achived {SCORES} points.")
