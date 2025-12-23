import requests
from requests.auth import HTTPBasicAuth
from PIL import Image
from colorama import Fore, Style, init

init(autoreset=True)

API_KEY ="acc_4c4387a89ac6c74" 
API_secret ="2ea16457d6847533ab53ca67f4e40ba2"
URL = "https://api.imagga.com/v2/text"

def truncate_text(text, word limit):
    words = text.split()
    return ' '.join(words[:word_limit])

def get_image_text(image_path):
    with open(image_path, 'rb') as img:
        responce = requests.post(
        IMAGGA_API_URl=
        auth=HTTPBasicAuth(API_KEY, API_secret),
        files={'image': img}
    )
        
        data = responce.json()
        tags = data.get('result', {}).get('text', [])
        return {tags['text']['en'] for tag in tags}
    
def generate_cation(tags):
    return truncate_text(", ".join(tags), 20)

def generate_discription(tags):
    sentences = ( 
    {f"THIS IMAGE SHOWS {tags[0]} "}
    {f"IT INCLUDES ELEMENTS SUCH AS {', '.join(tags[1:6])}."}
    {f"SCENE APPEARS TO BE CLEAR AND WELL COMPOSED"}
    )
    return truncate_text(sentences = 30)