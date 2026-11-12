import requests

respones = requests.get("https://api.github.com")
print(respones.status_code)


#This is a comment in Python
#varibale is a lebelled box where we can store data.

name = "John"
age = 30

#Varibale naming conventions:

user_name = "Alice"  # Use lowercase letters and underscores for variable names
userAge = 25        # Camel case is also acceptable, but less common in Python

grade2= "A"  # Avoid starting variable names with numbers
2grade = "B"  # This will cause a syntax error because variable names cannot start with numbers

my-name= "Bob"  # This will cause a syntax error because hyphens are not allowed in variable names
_name