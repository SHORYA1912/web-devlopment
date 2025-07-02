# india_quiz.py

def main():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
            "answer": "B"
        },
        {
            "question": "Who is known as the Father of the Nation in India?",
            "options": ["A) Jawaharlal Nehru", "B) Mahatma Gandhi", "C) Sardar Patel", "D) Bhagat Singh"],
            "answer": "B"
        },
        {
            "question": "Which river is considered the holiest in India?",
            "options": ["A) Yamuna", "B) Godavari", "C) Ganga", "D) Narmada"],
            "answer": "C"
        },
        {
            "question": "Which is the largest state in India by area?",
            "options": ["A) Maharashtra", "B) Uttar Pradesh", "C) Rajasthan", "D) Madhya Pradesh"],
            "answer": "C"
        },
        {
            "question": "Who wrote the Indian national anthem?",
            "options": ["A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Sarojini Naidu", "D) Subhash Chandra Bose"],
            "answer": "A"
        },
        {
            "question": "Which festival is known as the festival of lights?",
            "options": ["A) Holi", "B) Diwali", "C) Eid", "D) Christmas"],
            "answer": "B"
        },
        {
            "question": "What is the national animal of India?",
            "options": ["A) Lion", "B) Tiger", "C) Elephant", "D) Peacock"],
            "answer": "B"
        },
        {
            "question": "Which monument is known as the symbol of love?",
            "options": ["A) Qutub Minar", "B) Red Fort", "C) Taj Mahal", "D) India Gate"],
            "answer": "C"
        },
        {
            "question": "Who was the first Prime Minister of India?",
            "options": ["A) Indira Gandhi", "B) Rajendra Prasad", "C) Jawaharlal Nehru", "D) Lal Bahadur Shastri"],
            "answer": "C"
        },
        {
            "question": "Which is the national bird of India?",
            "options": ["A) Sparrow", "B) Parrot", "C) Peacock", "D) Eagle"],
            "answer": "C"
        }
    ]

    score = 0
    print("Welcome to the India Quiz!\n")
    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for opt in q['options']:
            print(opt)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    print(f"Quiz Over! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()