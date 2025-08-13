import colorama 
import random
from colorama import Fore, init

init(autoreset=True)

gamestypes = {
    "combat":["FREE FIRE","PUBG","CALL OF DUTY"],
    "open world":["FALL OUT 4","GTA5","ASSASSIN'S CREED"],
    "friendly":["ROBLOX","PLAY TOGETHER","MINECRAFT"],
    "strategy":["CLASH OF CLANS","RAID SHADOW LEGENDS","STARCRAFT 2"],
    "puzzle":["CANDY CRUSH","TETRIS","MONUMENT VALLEY"]

}

def normalize(text):
    return text.strip().lower()

def recommend():
    print(Fore.CYAN + "GAMEbot:  What type of game are you interested in? (combat, open world, friendly, strategy, puzzle)?")
    choice = normalize(input("> "))
    if choice in gamestypes:
        suggestions = random.choice(gamestypes[choice])
        print(Fore.GREEN + f"GAMEbot: How about PLAYINY {suggestions}?")
    else:
        print(Fore.RED + "GAMEbot: I'm sorry, I don't have recommendations for that category.")

def chat():
    user_input = normalize(input(Fore.YELLOW + "> "))
    if "recommend" in user_input:
        recommend()
    elif "bye" in user_input:
        print(Fore.CYAN + "GAMEbot :SAVES THE GAME")
    else:
        print(Fore.RED + "GAMEbot: I'm sorry, I didn't understand that.")
        chat()

if __name__ == "__main__":
    chat()
