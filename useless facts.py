import requests 
url = "https://uselessfacts.jsph.pl/random.json?language=en"

def get_random_facts():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
    
        print("CHOICES ARE [SCIENCE, HISTORY, MATH, GENERAL, TECHNOLOGY]")
        catagory = input("ENTER YOUR CHOICE OF CATAGORY: ").upper()

        if catagory == "SCIENCE":
            print(f"DID YOU KNOW? {fact_data['text']} (Category: Science)")
        elif catagory == "HISTORY":
            print(f"DID YOU KNOW? {fact_data['text']} (Category: History)")
        elif catagory == "MATH":
            print(f"DID YOU KNOW? {fact_data['text']} (Category: Math)")
        elif catagory == "GENERAL":
            print(f"DID YOU KNOW? {fact_data['text']} (Category: General)")
        elif catagory == "TECHNOLOGY":
            print(f"DID YOU KNOW? {fact_data['text']} (Category: Technology)")

        else:
            print("INVALID CATAGORY. PLEASE CHOOSE FROM THE GIVEN OPTIONS.")

while True:
        user_input = input("PRESS ENTER TO GET RANDOM FACTS OR TYPE q TO EXIT: ").upper()
        if user_input == "q":
            print("Exiting the program. Goodbye!")
            break
        get_random_facts()