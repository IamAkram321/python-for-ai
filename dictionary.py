"""
Dictionary: A dictionary is a collection of data stored in key-value pairs.

Characteristics of Dictionaries:
1. Dictionaries are created using curly brackets {}.
2. They store data in key-value pairs.
3. They are ordered (maintain insertion order).
4. They are mutable (we can add, remove, and update elements).
5. Keys must be unique.
6. Values can be duplicated and can have different data types.

Example:
student = {
    "name": "Akram",
    "age": 23,
    "marks": 85
}
print(student)
Output: {'name': 'Akram', 'age': 23, 'marks': 85}


2. Creating a Dictionary
 Dictionary of student details
 student = {
    "name": "Ram",
    "age": 18,
    "grade": 12
 }

Empty dictionary
my_dict = {}

Dictionary with different data types
 person = {
        "name": "Akram",
        "age": 23,
        "is_student": True,
        "marks": 85.5
    }



3. Accessing Dictionary Elements
We can access dictionary values using their keys.
student = {    
    "name": "Akram",    
    "age": 23,    
    "marks": 85
}
print(student["name"])
print(student["age"])



Output:
Akram
23


Using get(): Returns the value of a specified key. If the key does not exist, it returns None by default instead of raising a KeyError.

student = {"name": "Akram", "age": 23}
print(student.get("name"))
print(student.get("grade"))



Output:
Akram
None


4. Adding and Updating Elements: We can add a new key-value pair or update an existing value.
student = {    
    "name": "Akram",    
    "age": 23
} 
Adding a new element
student["marks"] = 85 

Updating an existing element
student["age"] = 24print(student)

Output:
{'name': 'Akram', 'age': 24, 'marks': 85}



5. Dictionary Methods
A. Methods to Access Elements
1. keys(): Returns all the keys in a dictionary.

student = {"name": "Akram", "age": 23, "marks": 85}
print(student.keys())
Output: dict_keys(['name', 'age', 'marks'])


2. values(): Returns all the values in a dictionary.

print(student.values())
Output: dict_values(['Akram', 23, 85])


3. items(): Returns all key-value pairs as tuples.

print(student.items())
Output: dict_items([('name', 'Akram'), ('age', 23), ('marks', 85)])


B. Methods to Add and Update Elements
4. update(): Adds new key-value pairs or updates existing keys.

student = {"name": "Akram", "age": 23}
student.update({"marks": 90, "age": 24})
print(student)
Output: {'name': 'Akram', 'age': 24, 'marks': 90}


5. setdefault(): Returns the value of a key. If the key does not exist, it adds the key with the specified default value.

student = {"name": "Akram", "age": 23}
student.setdefault("grade", 12)
print(student)
Output: {'name': 'Akram', 'age': 23, 'grade': 12}


C. Methods to Remove Elements
6. pop(): Removes a specified key and returns its value.

student = {"name": "Akram", "age": 23, "marks": 85}
removed = student.pop("age")
print("Removed:", removed)print(student)
Output:
Removed: 23
{'name': 'Akram', 'marks': 85}


7. popitem(): Removes and returns the last inserted key-value pair.

student = {"name": "Akram", "age": 23, "marks": 85}
print(student.popitem())
print(student)
Output:
('marks', 85)
{'name': 'Akram', 'age': 23}


8. clear(): Removes all elements from the dictionary.

student = {"name": "Akram", "age": 23}
student.clear()
print(student)
Output: {}


D. Method to Copy a Dictionary
9. copy(): Creates a shallow copy of an existing dictionary.

student = {"name": "Akram", "age": 23}
new_student = student.copy()
new_student["age"] = 24print("Original:", student)
print("Copied:", new_student)

Output:
Original: {'name': 'Akram', 'age': 23}
Copied: {'name': 'Akram', 'age': 24}



6. Looping Through a Dictionary
Using a for loop to access keys:

student = {"name": "Akram", "age": 23, "marks": 85}
for key in student:    
    print(key)



Accessing values:
for value in student.values():    
    print(value)



Accessing both keys and values:
for key, value in student.items():    
    print(key, ":", value)


Output:
name : Akram
age : 23
marks : 85


7. Checking Whether a Key Exists
We can use the in operator to check whether a key exists in a dictionary.

student = {"name": "Akram", "age": 23}
if "name" in student:    
    print("Key exists")
else:    
    print("Key does not exist")

Output: Key exists


8. Sample Programs
Program 1: Create a student details dictionary and display all details.

student = {    
    "name": "Ram",    
    "age": 18,    
    "marks": 85
}
for key, value in student.items():    
    print(key, ":", value)



Program 2: Find the total marks of students.

marks = {    
    "Ram": 80,    
    "Hari": 90,    
    "Sita": 85
}

total = 0
for mark in marks.values():    
    total += mark
print("Total marks:", total)



Program 3: Find the student with the highest marks.

marks = {    
    "Ram": 80,    
    "Hari": 95,    
    "Sita": 85
}
highest = max(marks, key=marks.get)
print("Topper:", highest)
print("Marks:", marks[highest])



Program 4: Count the frequency of each character in a string.

text = "hello"
frequency = {}
for char in text:    
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)

Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


"""
