# Implement a quiz game with at least 5 questions.

Questions = [
    "What is the Manchaster of Pakistan?",
    "Which City is called Roof of the World?",
    "What is the Capital of Japan?",
    "Which was the 1st man made canal?",
    "Which country is home to the pyramids of Giza?"
]

Answers = [
    "faisalabad",
    "tibet",
    "tokyo",
    "panama",
    "egypt"
]

score = 0

print("\n---- Welcome to the Quiz Game ----")

for i, question in enumerate(Questions, start = 1):
    print(f"\n{i}. {Questions[i-1]}")
    user_answer = input("Enter your Answer: ").lower()
    if user_answer == Answers[i-1]:
        print("Correct Answer.")
        score += 1
    else:
        print("Wrong Answer.")
        print(f"Correct Answer is '{Answers[i-1]}'")

print(f"Your Score is {score} out of {len(Questions)}.")
