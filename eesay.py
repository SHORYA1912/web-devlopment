import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt, temperature=0.3):
    try:
        res = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=800
        )
        return res.text.strip()
    except Exception as e:
        return f"error: {str(e)}"
    
def get_essay_details():
    print("\n" + "-" * 65 + "ESSAY WRITING ACTIVITY" + "-" * 65 + "\n") 

    topic = input("ENTER THE TOPIC FOR THE ESSAY: ").strip()
    essay_type = input("ENTER THE TYPE OF THE ESSAY: ").strip()
    length = input("ENTER THE DESIRED LENGTH OF THE ESSAY (IN WORDS): ").strip()
    audience = input("ENTER THE TARGET AUDIENCE FOR THE ESSAY: ").strip()

    return topic, essay_type, length, audience

def generate_essay(topic, essay_type, length, audience):
    try:
        temp = float(input("ENTER THE DESIRED TEMPERATURE (0.0-1.0): ").strip())
        if not 0.0 <= temp <= 1.0:
            temp = 0.3
    except ValueError:
        temp = 0.3

    prompt = f"Write an introduction for an essay on '{topic}' for {audience}. Essay type: {essay_type}, target length: {length} words."
    essay = generate_response(prompt, temp)
    print("\nGENERATED ESSAY:\n", essay)

def main():
    print("\nAI WRITING ASSISTANT\n")
    topic, essay_type, length, audience = get_essay_details()
    
    if all([topic, essay_type, length, audience]):
        generate_essay(topic, essay_type, length, audience)
    else:
        print("Please provide all required details.")

if __name__ == "__main__":
    main()
