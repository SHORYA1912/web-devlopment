import requests
from config import hf__api_key

def classify_text(text):
    API_URL= "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

    headers = {"Authorization": f"Bearer {hf__api_key}"}
    payload ={"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    print("RAW RESPONSE:", response.text)

    try:

        return response.json()

    except:

        return {"error": "Invalid JSON response"}

if __name__ == "__main__":
    sample_text = "I LOVE HUGGING FACE API"
    result = classify_text(sample_text)
    print("Sentiment Analysis Result:", result)

    


