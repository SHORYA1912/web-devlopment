from click import prompt
import cohere
import config
import time

co = cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt,temperature=0.3,max_TOKENS= 400):
    print("-------------------------GENERATE RESPONSE USING COHERE-------------------\n")
    try:
        res=co.chat(
        model="c4ai-aya-expanse-8b",
        message=prompt,
        temperature=temperature,
        max_tokens=max_TOKENS
        )

        return res.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
    
def bias_mitigation_activity():
    print("\n -------------------BIAS MITIGATION ACTIVITY-------------------\n")
    prompt = input("ENTER ANY PROMPT,LIKE EXAMPLE: `DESCIBE THE IDEAL DOCTOR`:")
    if not prompt:
        print("Please enter a valid prompt.")
        return
    
    initial = generate_response(prompt)
    print("\nINITIAL AI RESPONSE : ", initial)
    neutral = input("\n REWRITE IT IN THE NEUTRAL FORM:")
    print("\nNEUTRAL RESPONSE: ", neutral)
    if neutral:
        improved = generate_response(neutral)
        print("\n NEUTRAL AI RESP1ONSE:", improved)
    else:
        print("no input. Please enter a neutral prompt.")

def main():
    print("\n AI PROMPT ENGINEERING ACTIVITIES\n")
    print("1. Bias Mitigation Activity")
    print("2. EXIT")

    chioce = input("Enter your choice (1-2): ")
    if chioce == '1':
        bias_mitigation_activity()
    elif chioce == '2':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
