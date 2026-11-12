import requests

respones = requests.get("https://api.example.com/data")
print(respones.json())