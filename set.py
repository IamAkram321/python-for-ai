"""
Set: A set is a collection of unique elements stored in a single variable.

Characteristics of Sets:
1. Sets are created using curly brackets {}.
2. Sets are unordered (do not guarantee insertion order).
3. Sets are mutable (we can add or remove elements).
4. Sets do not allow duplicate values.
5. Sets do not support indexing or slicing.

Example:

fruits = {"Apple", "Banana", "Mango"}
print(fruits)
Output (order may vary): {'Apple', 'Banana', 'Mango'}


2. Creating Sets

 Set of integers:
 numbers = {10, 20, 30, 40}

  Set of strings:
  names = {"Ram", "Hari", "Sita"}

  Mixed data types:
  my_set = {10, "Akram", 85.5, True}

  Empty set:
  empty_set = set()



Important: 
{} creates an empty dictionary, not an empty set. 
Use set() to create an empty set.

3. Duplicate Elements
Sets automatically remove duplicate elements.

numbers = {10, 20, 10, 30, 20}
print(numbers)
Output (order may vary):{10, 20, 30}


4. Adding Elements

add(): Adds one element to a set.

fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)

update(): Adds multiple elements from another iterable.

numbers = {10, 20}
numbers.update([30, 40, 50])
print(numbers)



5. Removing Elements
remove(): Removes a specified element. Gives an error if the element does not exist.

numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)


discard(): Removes a specified element without giving an error if it does not exist.

numbers = {10, 20, 30}
numbers.discard(50)
print(numbers)



pop(): Removes and returns an arbitrary element.

numbers = {10, 20, 30}
removed = numbers.pop()
print("Removed:", removed)
print(numbers)



clear(): Removes all elements.

numbers = {10, 20, 30}
numbers.clear()
print(numbers)
Output: set()

6. Set Operations: Set operations are used to compare and combine two sets.

Let us consider:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

1. Union (|): Combines all unique elements from both sets.
print(A | B)
Output (order may vary): {10, 20, 30, 40, 50, 60}

2. Intersection (&): Returns common elements from both sets.
print(A & B)
Output: {30, 40}

3. Difference (-): Returns elements present in the first set but not in the second.
print(A - B)
Output: {10, 20}

4. Symmetric Difference (^)
Returns elements that are present in either set, but not in both.
print(A ^ B)
Output (order may vary): {10, 20, 50, 60}


7. Other Useful Set Methods
Method	                            Purpose
len()	           Returns the number of elements (built-in function)
copy()	           Creates a shallow copy
issubset()	   Checks whether all elements of one set exist in another
issuperset()	Checks whether a set contains all elements of another
isdisjoint()	Checks whether two sets have no common elements

Example:

A = {10, 20, 30}
B = {10, 20}
print(B.issubset(A))            True
print(A.issuperset(B))          True
print(A.isdisjoint({40, 50}))   True



8. Looping Through a Set
We can use a for loop to access elements.

fruits = {"Apple", "Banana", "Mango"}
for fruit in fruits:    
    print(fruit)


9. Sample Programs
Program 1: Remove duplicate values from a list.

numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = set(numbers)
print(unique_numbers)



Program 2: Find common elements between two sets.

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
common = A.intersection(B)
print("Common elements:", common)



Program 3: Check whether an element exists.
fruits = {"Apple", "Banana", "Mango"}
if "Mango" in fruits:    
    print("Fruit found")
else:    
    print("Fruit not found")


"""