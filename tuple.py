"""
Tuple: A tuple is a collection of multiple elements stored in a single variable.

Characteristics of Tuples:
1. Tuples are created using parentheses ().
2. Tuples are ordered (elements have index numbers).
3. Tuples are immutable (cannot be modified after creation).
4. Tuples allow duplicate values.
5. Tuples can store different data types.

Example:

fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits)
Output: ('Apple', 'Banana', 'Mango', 'Orange')


2. Creating Tuples

Tuple of strings
names = ("Akram", "Ram", "Hari")

Tuple of integers
numbers = (10, 20, 30, 40)

Mixed data types
student = ("Akram", 23, 85.5, True) 

 Empty tuple
 my_tuple = () 

 Single-element tuple (comma is necessary)
 single = (10,)

Important: (10) is an integer, not a tuple. (10,) is a tuple.

3. Accessing Tuple Elements (Indexing)
Tuple indexing starts from 0.

fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits[0])    Apple
print(fruits[2])    Mango
print(fruits[-1])   Orange



4. Tuple Slicing
Slicing is used to access a portion of a tuple.

Syntax: tuple_name[start:end]

The ending index is excluded.
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

Output:
(20, 30, 40)
(10, 20, 30)
(30, 40, 50)


5. Tuple Immutability
Tuples cannot be modified after creation.
fruits = ("Apple", "Banana", "Mango")
fruits[1] = "Grapes"
print(fruits)
Output:
TypeError: 'tuple' object does not support item assignment


Unlike lists, we cannot directly add, remove, or update tuple elements.

6. Tuple Methods
Tuples have only two built-in methods because they are immutable.

1. count()
Returns the number of times an element appears in a tuple.

numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))
Output: 3


2. index()
Returns the index of the first occurrence of an element.
fruits = ("Apple", "Banana", "Mango", "Banana")
print(fruits.index("Banana"))

Output: 1

7. Useful Built-in Functions with Tuples
Function	        Purpose
len()	    Returns the number of elements
max()	    Returns the largest element
min()	    Returns the smallest element
sum()	    Returns the sum of numeric elements
sorted()	Returns a new sorted list

Example:
numbers = (10, 50, 20, 40, 30)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

Output:
5
50
10
150
[10, 20, 30, 40, 50]

Note: sorted() returns a list, not a tuple.

8. Looping Through a Tuple
We can use a for loop to access every element.

fruits = ("Apple", "Banana", "Mango")
for fruit in fruits:    
    print(fruit)



Output:
Apple
Banana
Mango


9. Tuple Packing and Unpacking
Packing: Storing multiple values in a single tuple.
student = ("Akram", 23, 85)



Unpacking: Assigning tuple elements to separate variables.
student = ("Akram", 23, 85)
name, age, marks = student
print(name)
print(age)
print(marks)

Output:
Akram
23
85



10. Sample Programs

Program 1: Find the sum of tuple elements.

numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:    
    total += num
print("Total:", total)



Program 2: Find the largest number without using max().
numbers = (15, 45, 10, 80, 25)
largest = numbers[0]
for num in numbers:    
    if num > largest:        
        largest = num
print("Largest:", largest)



Program 3: Search for an element in a tuple.

fruits = ("Apple", "Banana", "Mango")
search = input("Enter a fruit: ")
if search in fruits:    
    print("Fruit found")
else:    
    print("Fruit not found")



Program 4: Count even and odd numbers.

numbers = (10, 15, 20, 25, 30, 35)
even = 0
odd = 0
for num in numbers:    
    if num % 2 == 0:        
        even += 1    
    else:        
        odd += 1
print("Even:", even)
print("Odd:", odd)




11. Difference Between List and Tuple
List	                                Tuple
Uses []	                                Uses ()
Mutable	                                Immutable
Has 11 common methods	                Has 2 methods
Can add, remove and update elements	    Cannot directly add, remove or update elements
Example: [10, 20, 30]	                Example: (10, 20, 30)

"""