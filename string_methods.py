name = " i am akRam "

#Case Modification

print(name.lower())
print(name.upper()) #coverts all characters to uppercase
print(name.capitalize()) #converts only the first character to uppercase and others will be forced to be lowercase

print(name.title()) #capitalizes first letter of every word
print(name.swapcase()) #swaps lowercase to upper and vice-versa

print(name.casefold()) # coverts string to lowercase(aggressive, best for matching unicode)

#Searching and Counting

fruit = "banana"
fruit.count("an") #returns the number of times a substring occurs.
fruit.find("os") #returns the lowest index of substring, or -1 if not found.
fruit.rfind("an") #returns the highest index of substring, or -1 if not found.

fruit.index("p") #Like find(), but raises a ValueError if not found.
fruit.rindex("p") #Like rfind(), but raises a ValueError if not found.

job = " I am a lawyer "
print(job.strip())
print(job.lstrip()) #removes leading whitespaces
print(job.rstrip()) #removes trailing whitespaces
print(job.replace("lawyer", "doctor"))

#Character Checks (Validation)
name = "akram2_"
num = "123"
a = "1.5"
print(name.isalnum()) #All characters are alphanumeric (letters or numbers).

print(name.isdigit()) #all characters are digits
print(name.isalpha()) #all characters are alphabets
print(num.isnumeric()) #all characters are numbers
print(a.isdecimal()) #all characters are decimals (plain numbers 0-9).

