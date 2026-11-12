import requests

respones = requests.get("https://api.github.com")
print(respones.status_code)