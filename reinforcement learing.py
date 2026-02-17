import cohere
import config
import time

co = cohere.Client(config.COHERE_API_KEY)   

def get_ai_response(prompt, temperature=0.5):
    
        try:
            res=co.chat(
            model="command-r",
            message=prompt,
            temperature=temperature,
            max_tokens=200
            )

            return res.text.strip()
        except Exception as e:
            return f"Error: {str(e)}"
    
def feedback_activity():
    print("\n -------------------FEEDBACK BASED LEARNING-------------------\n")
    prompt = input("enter a prompt for the ai to respond to:")
    ans = get_ai_response(prompt)
    print("\n AI RESPONSE: ", ans)

    rating = input("\nRate the response on a scale of 1-5 (1=Poor, 5=Excellent): ")
    feedback = input("Provide specific feedback to improve the response: ")
    print("\nThank you for your feedback! The AI will use this to improve future responses.")

    improvised = ans + "\n improved using feedback:" + feedback
    print("\nImprovised Response: ", improvised)

def role_activity():
    print("\n -------------------ROLE-BASED LEARNING-------------------\n")
    category = input("Enter a category (e.g., animal, food, city, science): ").strip()
    item = input(f"Enter a specific topic")

    teacher = f"You are a teacher explaining {item} in the context of {category} to a student. Provide a simple explanation suitable for a beginner."
    expert = f"You are an expert in {category} providing an in-depth analysis of {item}. Include advanced concepts and recent developments."
    
    print("\n--- TEACHER VIEW ---")
    print(get_ai_response(teacher))
    time.sleep(1)

    print("\n--- EXPERT VIEW ---")
    print(get_ai_response(expert))
    time.sleep(1)

def temperature_activity():
    print("\n -------------------TEMPERATURE BASED LEARNING-------------------\n")
    prompt = input("ENTER CREATIVE PROMPT:")

    for t in [0.1,0.5,0.9]:
        print(f"\n--- TEMPERATURE: {t} ---")
        get_ai_response(prompt, temperature=t)
        time.sleep(1)

def main():
     while True:
        print("\n-------------------AI LEARNING ACTIVITIES-------------------\n")
        print("1. Feedback-Based Learning")
        print("2. Role-Based Learning")
        print("3. Temperature-Based Learning")
        print("4. Exit")

        choice = input("\nSelect an activity (1-4): ")

        if choice == '1':
            feedback_activity()
        elif choice == '2':
            role_activity()
        elif choice == '3':
            temperature_activity()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            

        else:
            print("INVALID CHOICE")
if __name__=="__main__":
    main()