import colorama 
import random
from colorama import Fore, init

init(autoreset=True)

destination = {
    "beaches":["BALI","MALDIVES","PHUKET"],
    "mountains":["HIMALAYAS","ALPS","ROCKY MOUNTAINS"],
    "cities":["PARIS","NEW YORK","TOKYO"]

}

def normalize(text):
    return text.strip().lower()

def recommend():
    print(Fore.CYAN + "travelbot: Beaches, mountains, or cities?")
    choice = normalize(input("> "))
    if choice in destination:
        suggestions = random.choice(destination[choice])
        print(Fore.GREEN + f"travelbot: How about visiting {suggestions}?")
    else:
        print(Fore.RED + "travelbot: I'm sorry, I don't have recommendations for that category.")

def travel_tips():
    location = input(Fore.YELLOW + "destination")
    days = input(Fore.YELLOW + " HOW MANY DAYS")
    print(Fore.GREEN + f"travelbot: For your trip to {location} for {days} days, make sure to pack accordingly and check the weather forecast!")
    print("--check the weather forecast--")
    print("--pack versatile cloths--")
    print("--don't forget charger and id--")

def chat():
    user_input = normalize(input(Fore.YELLOW + "> "))
    if "recommend" in user_input:
        recommend()
    elif "tip" in user_input:
        travel_tips()
    elif "bye" in user_input:
        print(Fore.CYAN + "travel bot :saves the Travel")
    else:
        print(Fore.RED + "travelbot: I'm sorry, I didn't understand that.")
        chat()

if __name__ == "__main__":
    chat()
