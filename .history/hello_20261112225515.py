import requests

respones = requests.get("https://api.github.com")
print(respones.status_code)


#This is a comment in Python
""" This is a multiline 
comment in python. It can span multiple lines and is often used for documentation purposes. """