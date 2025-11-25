import requests
import random
import html
import sys

EDUCATION_CATEGORY_ID = 9
AMOUNT = 10
API_BASE = "https://opentdb.com/api.php"

def get_education_questions(amount=AMOUNT):
    params = {"amount": amount, "category": EDUCATION_CATEGORY_ID, "type": "multiple"}
    try:
        response = requests.get(API_BASE, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        return []
    data = response.json()
    if data.get("response_code") == 0 and data.get("results"):
        return data["results"]
    return []

def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("Failed to retrieve questions. Please try again later.")
        return
    score = 0
    print("Welcome to the Education Quiz! (type 'q' to quit at any prompt)")
    try:
        for i, q in enumerate(questions, start=1):
            question_text = html.unescape(q.get("question", ""))
            correct_answer = html.unescape(q.get("correct_answer", ""))
            incorrect_answers = [html.unescape(ans) for ans in q.get("incorrect_answers", [])]
            options = incorrect_answers + [correct_answer]
            random.shuffle(options)

            print(f"\nQuestion {i}: {question_text}")
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            while True:
                user_input = input("Your answer (1-4 or 'q' to quit): ").strip().lower()
                if user_input == "q":
                    print("Quiz exited by user.")
                    print(f"Final score: {score}/{i-1} ({(score/(i-1)*100) if i>1 else 0:.1f}%)")
                    return
                try:
                    choice = int(user_input)
                except ValueError:
                    print("Please enter a number corresponding to an option, or 'q' to quit.")
                    continue
                if 1 <= choice <= len(options):
                    break
                print("Invalid choice. Please select a valid option number.")

            if options[choice - 1] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")

    except KeyboardInterrupt:
        print("\nQuiz interrupted.")
    finally:
        total_answered = i if 'i' in locals() else 0
        print(f"\nFinal score: {score}/{total_answered} ({(score/total_answered*100) if total_answered else 0:.1f}%)")

if __name__ == "__main__":
    run_quiz()