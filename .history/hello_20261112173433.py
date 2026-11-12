import requests

respones = requests.get("https://api.github.com/data")
print(respones.json())