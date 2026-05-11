# General Knowledge Quiz Game in Python

print("🧠 Welcome to the GK Quiz Game!")
print("--------------------------------")

score = 0

# List of questions and answers
questions = [
    {
        "question": "1. What is the capital of India?",
        "answer": "delhi"
    },
    {
        "question": "2. Who invented the telephone?",
        "answer": "alexander graham bell"
    },
    {
        "question": "3. Which planet is known as the Red Planet?",
        "answer": "mars"
    },
    {
        "question": "4. How many continents are there on Earth?",
        "answer": "7"
    },
    {
        "question": "5. What is the largest ocean in the world?",
        "answer": "pacific"
    }
]

# Quiz loop
for q in questions:
    print("\n" + q["question"])
    user_answer = input("Your answer: ").lower()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct answer:", q["answer"].title())

# Final score
print("\n--------------------------------")
print("🎯 Quiz Finished!")
print("Your score:", score, "/", len(questions))

# Performance message
if score == len(questions):
    print("🏆 Excellent! Perfect score!")
elif score >= 3:
    print("👍 Good job!")
else:
    print("📚 Keep learning and try again!")