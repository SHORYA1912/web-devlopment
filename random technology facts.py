import requests
url = "https://uselessfacts.jsph.pl/random.json?language=en"
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"DID YOU KNOW?{fact_data['text']}")

while True:
        user_input = input("PRESS ENTER TO GET RANDOM TECHNOLOGY FACTS OR TYPE q TO EXIT")
        if user_input == "q":
            print("Exiting the program. Goodbye!")
            break
        get_random_technology_fact()
