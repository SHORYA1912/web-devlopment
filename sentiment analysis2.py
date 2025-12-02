import requests

url = "https://sentim-api.onrender.com/api/v1/"

headers = {'ACCEPT': 'application/json', 'CONTENT_TYPE': 'application/json'}
data = {'text': 'you are a bad person.'}
response = requests.post(url, headers=headers, json=data)

print(response.json())
