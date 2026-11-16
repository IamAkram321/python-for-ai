"""

Module  : A single python file like (hello.py)
Package : A folder containing multiple modules
Function: A reusable block of code (like print() or sqrt())

"""

#Pattern 1: Import the whole module

import math
root = math.sqrt(25)
print(root)

#random values
import random
number = random.randint(1,10)
choice = random.choice(["apple", "banana", "guava", "grapes"])
print(number)
print(choice)

#date and time

import datetime
today = datetime.datetime.today()
print(today.day)
print(today)

#operating system

import os
current_dir = os.getcwd()
print(current_dir)

#JSON data

import json
data = {"name": "Alice", "age": 18}
print(data)
json_string = json.dumps(data)
print(json_string)

#pattern 2: Import some specific items from module

from math import sqrt, pi
radius = 16
area   = pi * radius * radius
print(area)
print(sqrt(radius))







