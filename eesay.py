import cohere
import config

co = cohere.Client(config.COHERE_API_KEY)

def generate_responce(prompt, temperature=0.3):
    try:
        res=co.chat(
        model="c4ai-aya-expanse-8b",
        message=prompt,
        temperature=temperature,
        max_tokens=800
        )

        return res.text.strip()
    except Exception as e:
        return f"error: {str(e)}"
    
def get_essay_details():
    print("\n-------------------------ESSAY WRITTING ACTIVITY-------------------\n") 

    topic = input("ENTER THE TOPIC FOR THE ESSAY: ")
    essay_type = input("ENTER THE TYPE OF THE ESSAY:  ")
    lenght = input("ENTER THE DESIRED LENGHT OF THE ESSAY (IN WORDS): ")
    audience = input("ENTER THE TARGET AUDIENCE FOR THE ESSAY: ")

    return topic, essay_type, lenght, audience

def generate_essay( topic, essay_type, lenght, audience):
    try:
        temp = float(input("ENTER THE DESIRED TEMPERATURE (0.0-1.0):").strip())
    except:
        temp = 0.3

    section = (f"write an introduction for the essay on the topic {topic} for the {audience} audience. The essay should be of type {essay_type} and should be around {lenght} words long.")

    essay = generate_responce(section, temp)
    print("\n GENERATED ESSAY:\n", essay)

def main():
    print("\n AI WRITING ASSISTANT ACTIVITIES\n")
    TOPIC, ESSAY_TYPE, LENGHT, AUDIENCE = get_essay_details()
    
    if TOPIC and ESSAY_TYPE and LENGHT and AUDIENCE:
        generate_essay(TOPIC, ESSAY_TYPE, LENGHT, AUDIENCE)
    else:
        print("Please provide all the required details to generate the essay.")

if __name__ == "__main__":
    main()   
