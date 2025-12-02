import requests

url = "https://sentim-api.onrender.com/api/v1/"

headers = {'APPCEPT': 'application/json'}
{'CONTENT_TYPE': 'application/json'}

data = {'text': 'I love programming in Python! It is such a versatile language.'}
responcese = requests.post(url, headers=headers, json=data)
print(responcese.json())

