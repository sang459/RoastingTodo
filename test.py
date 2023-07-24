import requests

url = "https://deepl-translator.p.rapidapi.com/translate"

payload = {
	"text": "This is a example text for translation.",
	"source": "EN",
	"target": "KO"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "c4b6c9c6a4msh3675a0ba0be3804p1c4e14jsn4b57c627b6cf",
	"X-RapidAPI-Host": "deepl-translator.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()['text'])