import requests
from requests.auth import HTTPBasicAuth

API_KEY ="acc_4c4387a89ac6c74" 
API_secret ="2ea16457d6847533ab53ca67f4e40ba2" 

def caption_single_image(image_path):
    url = "https://api.imagga.com/v2/tags"

    with open(image_path, 'rb')as img:
        responce = requests.post(
            url,
            auth=HTTPBasicAuth(API_KEY, API_secret),
            files={'image': img}
        )

    data = responce.json()
    tags = data.get('result', {}).get('tags', [])
    captions = [tag['tag']['en'] for tag in tags]

    print("Image", image_path)
    print("Caption (generated from image):", ", ".join(captions))

def main():
 image_path = input("Enter the path to the image file: ")
 caption_single_image(image_path)

if __name__ == "__main__":
    main()
 
 
