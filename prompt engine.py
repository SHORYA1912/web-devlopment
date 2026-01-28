import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

def generate_responce(prompt):
    try:
        response = co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            max_tokens=200,
            temperature=0.7,
        )

        return response.text.strip()
    except Exception as e:
        return f"Error generating response: {str(e)}"

def prompt_enginniering_project():
    print("Welcome to the Prompt Engineering Project!")
    print("=" * 60)
    print("ASK ANY QUESTION ASND GET ANSWERS LIKE AI")
    print("=" * 60)

    user_prompt = input("Enter your prompt: ")

    print("\nGenerating AI response...\n")
    print(generate_responce(user_prompt))

if __name__ == "__main__":
    prompt_enginniering_project()


        