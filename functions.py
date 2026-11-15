"""
Function: A function is a block of reusable code that performs a specific task.

Instead of writing the same code repeatedly, we can create a function and call it whenever needed.

Advantages of Functions:
1. Code reusability.
2. Reduces code repetition.
3. Makes programs easier to understand.
4. Makes debugging and maintenance easier.

2. Types of Functions
Python functions are mainly divided into two types:

1. Built-in Functions: Functions already available in Python, such as print(), len(), sum(), max().
2. User-defined Functions: Functions created by programmers using the def keyword.


3. Creating a Function
We use the def keyword to define a function.

Syntax:
def function_name():    
    # Statements    
    # Function body



Example:

def greet():    
    print("Hello, Welcome to Python!")
greet()
Output: Hello, Welcome to Python!


Explanation:
- def is used to define a function.
- greet is the function name.
- () represents function parameters.
- The indented statements form the function body.
- greet() calls or executes the function.


4. Functions with Parameters
Parameters are variables that receive values when a function is called.

def greet(name):    
    print("Hello", name)
greet("Akram")
greet("Ram")

Output:
Hello Akram
Hello Ram


5. Functions with Multiple Parameters
A function can accept multiple parameters.

def add(a, b):    
    print("Sum:", a + b)
add(10, 20)

Output:
Sum: 30


6. Return Statement
The return statement sends a result back from a function.

def add(a, b):    
    return a + b
result = add(10, 20)
print("Sum:", result)

Output:
Sum: 30


Difference between print() and return:
- print() displays a value on the screen.
- return sends a value back to the place where the function was called.


7. Default Parameters
We can provide a default value to a parameter. If no argument is passed, Python uses the default value.
def greet(name="Student"):    
    print("Hello", name)
greet()
greet("Akram")

Output:
Hello Student
Hello Akram


8. Keyword Arguments
We can pass arguments using parameter names.

def student(name, age):    
    print("Name:", name)    
    print("Age:", age)
student(age=23, name="Akram")



Output:
Name: Akram
Age: 23


9. Local and Global Variables
Local Variable: A variable created inside a function. It can normally be accessed only inside that function.

Global Variable: A variable created outside a function. It can be accessed inside functions.

name = "Akram"  # Global variable
def greet():    
    age = 23    # Local variable    
    print(name)    
    print(age)
greet()



10. Sample Programs
Program 1: Check whether a number is even or odd.

def check_number(num):    
    if num % 2 == 0:        
        print("Even number")    
    else:        
        print("Odd number")
check_number(10)



Program 2: Find the largest of two numbers.

def largest(a, b):    
    if a > b:        
        return a    
    else:        
        return b
print("Largest:", largest(20, 50))



Program 3: Find the factorial of a number.

def factorial(num):    
    fact = 1    
    for i in range(1, num + 1):        
        fact = fact * i    
    return fact
print("Factorial:", factorial(5))



Program 4: Find the sum of numbers in a list.

def calculate_sum(numbers):    
    total = 0    
    for num in numbers:        
        total += num    
    return total
print(calculate_sum([10, 20, 30, 40]))

Output: 100



Practice Questions
1. Create a function to print your name.
2. Create a function to add two numbers.
3. Create a function to calculate the area of a rectangle.
4. Create a function to check whether a number is positive, negative, or zero.
5. Create a function to find the largest of three numbers.
6. Create a function to calculate the factorial of a number.
7. Create a function to check whether a number is prime.
8. Create a function to reverse a string.


"""
