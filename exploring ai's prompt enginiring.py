import time
import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt,temperature=0.5):
    """
    GENERATING RESPONSE
    """
    try:
        generate_response= co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            max_tokens=300,
            temperature=temperature,
        )
        return generate_response.text.strip()
    
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def temperature_prompt_activity():
    """
    INTERRECTIVE ACTIVITY TO DEMONSTRATE THE EFFECT OF TEMPERATURE ON AI RESPONCES, USING PROMPT ENGINEERING
    """
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE EFFECT DEMONSTRATION")
    print("=" * 80)

    print("in this activity , we will explore how the temperature parameter affects the creativity and diversity of AI responses.")
    print("1) Effect of temperature on AI responses and creativity")
    print("2) How instruction based prompt control AI outputs")

    print("\n" + "-" *  40)
    print("1) Effect of temperature on AI responses and creativity")
    print("-" * 40)

    base_prompt = input(
        "\n Enter creative prompt"
        "Write a sci-fi robot story"
    )

    print("\n LOW TEMPERATURE (0.1) DETERMINISTIC AND FOCUSED RESPONCES ")
    print("generate_responce"(base_prompt, temperature = 0.1))
    (time.sleep(1))

    print("\n MEDIUM TEMPERATURE (0.5) BALANCED CREATIVITY AND COHERENCE")
    print("generate_responce"(base_prompt, temperature = 0.5))
    (time.sleep(1))

    print("\n HIGH TEMPERATURE (0.9) CREATIVE AND DIVERSE RESPONCES")
    print("generate_responce"(base_prompt, temperature = 0.9))

    print("\n" + "-" * 40)
    print("2) How instruction based prompt control AI outputs")
    print("-" * 40)

    topic = input("\n Enter a topic for the AI to write about: ")

    instruction_prompt = {
        "Write a formal essay about the impact of technology on society.": "Formal and structured response",
        "Write a casual blog post about the impact of technology on society.": "Explain me as i am ten years old",
        "Write a creative story about the impact of technology on society.": "Creative and imaginative response"
    }

    for i , instruction in enumerate(instruction_prompt , start = 1):
        print("-----------------------INSTRUCTION------------------------")
        print(f"\n INSTRUCTION {i}: {instruction} - {instruction_prompt[instruction]}")
        print("generate_responce"(instruction))
        (time.sleep(1))

    print("\n" + "=" * 80)
    print("END OF TEMPERATURE EFFECT DEMONSTRATION")
    print("part-3 custom instruction + temperature control")
    print("=" * 80)

    custom_instruction = input("\n Enter a custom instruction for the AI: ")
    try:
            custom_temperature = float(input("Enter a temperature value (0.0 to 1.0): "))
            if not 0.0 <= custom_temperature <= 1.0:
                raise ValueError("Temperature must be between 0.0 and 1.0.")
    
    except ValueError as e:
        print(f"Invalid input for temperature: {e}")
        return
    