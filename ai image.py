from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import requests
from io import BytesIO

def generate_image(prompt):

    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"

    print("Fetching image from Pollinations...")
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def post_proccessing(image):
    image = ImageEnhance.Brightness(image).enhance(2.0)
    image = ImageEnhance.Contrast(image).enhance(1.5)
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return image

def main():
    print("POST-PROCESSING WORKSHOP (NO API IS NEEDED)")

    while True:
        text_prompt = input("Enter image prompt (or 'exit' to quit): ")
        if text_prompt.lower() == 'exit':
            print("GOODBYE")
            break

        img = generate_image(text_prompt)

        proccessed = post_proccessing(img)
        proccessed.show()

        save_option = input("Do you want to save the image? (y/n): ")
        if save_option.lower() == 'y':
            name = input("FILE NAME").strip()
            proccessed.save(f"{name}.png")
            print(f"Image saved as {name}")
        else:
            print("Image not saved.")

if __name__ == "__main__":
    main()