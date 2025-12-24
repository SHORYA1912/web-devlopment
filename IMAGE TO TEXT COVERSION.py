import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
import os
from colorama import init, Fore, Style

init(autoreset=True)


API_KEY ="acc_4c4387a89ac6c74" 
API_SECRET ="2ea16457d6847533ab53ca67f4e40ba2"
IMAGGA_URL = "https://api.imagga.com/v2/tags"


def truncate_text(text, word_limit):
    words = text.split()
    return " ".join(words[:word_limit])


def get_image_tags(image_path, limit=10):
    with open(image_path, "rb") as img:
        response = requests.post(
            IMAGGA_URL,
            auth=HTTPBasicAuth(API_KEY, API_SECRET),
            files={"image": img}
        )

    data = response.json()
    tags = data.get("result", {}).get("tags", [])
    return [tag["tag"]["en"] for tag in tags[:limit]]


def generate_caption(tags):
    return truncate_text(", ".join(tags), 5)

def generate_description(tags):
    sentence = (
        f"This image shows {tags[0]}. "
        f"It includes elements such as {', '.join(tags[1:6])}. "
        f"The scene appears visually clear and well composed."
    )
    return truncate_text(sentence, 30)

def generate_summary(tags):
    sentence = (
        f"The image primarily features {tags[0]}. "
        f"Other visible elements include {', '.join(tags[1:7])}. "
        f"The objects are clearly distinguishable and form a meaningful scene. "
        f"The image provides a simple yet informative visual representation."
    )
    return truncate_text(sentence, 50)

def print_menu():
    print(f"""{Style.BRIGHT}{Fore.GREEN}
================ IMAGE-TO-TEXT CONVERSION =================
Select output type:
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
===========================================================
""")

def main():
    image_path = input(f"{Fore.BLUE}Enter image path: {Style.RESET_ALL}")

    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ Image file not found.")
        return

    try:
        Image.open(image_path)
    except:
        print(f"{Fore.RED}❌ Invalid image file.")
        return

    print(f"{Fore.YELLOW}🔍 Analyzing image...\n")
    tags = get_image_tags(image_path)

    if not tags:
        print(f"{Fore.RED}❌ Failed to generate tags.")
        return

    while True:
        print_menu()
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            caption = generate_caption(tags)
            print(f"{Fore.YELLOW}📌 Caption (5 words): {Style.BRIGHT}{caption}\n")

        elif choice == "2":
            desc = generate_description(tags)
            print(f"{Fore.CYAN}📝 Description (30 words): {Style.BRIGHT}{desc}\n")

        elif choice == "3":
            summary = generate_summary(tags)
            print(f"{Fore.GREEN}📄 Summary (50 words): {Style.BRIGHT}{summary}\n")

        elif choice == "4":
            print(f"{Fore.GREEN}👋 Goodbye!")
            break

        else:
            print(f"{Fore.RED}❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
