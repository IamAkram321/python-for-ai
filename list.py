"""
1. What is a List?
A list is a collection of multiple elements stored in a single variable.

Characteristics of Lists:
1. Lists are created using square brackets [].
2. Lists are ordered (elements have index numbers).
3. Lists are mutable (we can modify elements).
4. Lists allow duplicate values.
5. Lists can store different data types.

Example:

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)
Output:['Apple', 'Banana', 'Mango', 'Orange']


2. Accessing List Elements (Indexing): Indexing is used to access individual elements from a list.

Python indexing starts from 0.
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])   # Apple
print(fruits[2])   # Mango
print(fruits[-1])  # Orange


3. Updating List Elements

Lists are mutable, so we can change their elements.
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Grapes"
print(fruits)

Output:
['Apple', 'Grapes', 'Mango']


4. List Slicing: Slicing is used to access a portion of a list.
Syntax: list_name[start:end]

The ending index is excluded.

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

Output:
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]



5. List Methods: List methods are built-in operations used to add, remove, search, and arrange elements in a list.

A. Methods to Add Elements

1. append(): Adds one element at the end of a list.

fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)
Output: ['Apple', 'Banana', 'Mango']

2. insert(): Adds an element at a specific index.

fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)
Output: ['Apple', 'Banana', 'Mango']

3. extend():Adds multiple elements from another iterable to the end of a list.

a = [10, 20]
b = [30, 40]
a.extend(b)
print(a)
Output: [10, 20, 30, 40]

Difference:
- append() adds the entire argument as one element.
- extend() adds the elements individually.

B. Methods to Remove Elements

4. remove(): Removes the first occurrence of a specified value.

numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)
Output: [10, 30, 20]


5. pop()
Removes and returns an element using its index. Without an index, it removes the last element.
numbers = [10, 20, 30, 40]
removed = numbers.pop(1)
print("Removed:", removed)
print(numbers)
Output:
Removed: [10, 30, 40]


6. clear():Removes all elements from a list.
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
Output: []


C. Methods to Search and Count

7. index(): Returns the index of the first occurrence of an element.

fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Mango"))
Output: 2

8. count(): Returns the number of times an element appears in a list.
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))
Output: 3


D. Methods to Arrange Elements

9. sort(): Sorts the elements in ascending order by default.
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
Output: [10, 20, 30, 40]

For descending order:
numbers.sort(reverse=True)print(numbers)
Output: [40, 30, 20, 10]


10. reverse(): Reverses the existing order of elements. It does not sort them.
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)
Output: [40, 30, 20, 10]


E. Method to Copy a List

11. copy(): Creates a shallow copy of an existing list.

numbers = [10, 20, 30]
new_numbers = numbers.copy()
new_numbers.append(40)
print("Original:", numbers)
print("Copied:", new_numbers)
Output:
Original: [10, 20, 30]
Copied: [10, 20, 30, 40]



6. Useful Built-in Functions with Lists
These are functions, not list methods.

Function	                  Purpose
len()	            Returns the number of elements
max()	            Returns the largest element
min()	            Returns the smallest element
sum()	            Returns the sum of numeric elements
sorted()	        Returns a new sorted list

Example:
numbers = [10, 50, 20, 40, 30]
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

Output:
Length: 5
Maximum: 50
Minimum: 10
Sum: 150
Sorted: [10, 20, 30, 40, 50]


7. Looping Through a List
We can use a for loop to access every element in a list.

fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:    
    print(fruit)

Output:
Apple
Banana
Mango


8. Sample Programs
Program 1: Find the sum of all elements in a list.

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:    
    total = total + num
    print("Total:", total)



Program 2: Find the largest number in a list.

numbers = [15, 45, 10, 80, 25]
largest = numbers[0]
for num in numbers:    
    if num > largest:        
        largest = numprint("Largest number:", largest)



Program 3: Count even and odd numbers.

numbers = [10, 15, 20, 25, 30, 35]
even = 0
odd  = 0
for num in numbers:    
    if num % 2 == 0:        
        even += 1    
    else:        
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)



Program 4: Search for an element in a list.

numbers = [10, 20, 30, 40, 50]
search = int(input("Enter a number: "))
if search in numbers:
    print("Element found")
else:
    print("Element not found")

"""