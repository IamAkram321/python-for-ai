"""
Operators: Operators: Operators are special symbols or keywords used to perform operations on variables and values.
There are 7 main types of operators in Python. They are:

1. Arithmetic Operators(+,-,*,**,/,//,%): Arithmetic operators are used to perform mathematical calculations. 

a = 5
b = 2

print(a + b)            #7
print(a - b)            #3
print(a * b)            #10
print(a / b)            #2.5
print(a % b)            #1
print(a ** b)           #25
print(a // b)           #2


2. Comparison Operators(==, >, >=, <, <=, !=): Comparison operators are used to compare two values. They return either True or False. 

a = 10
b = 5

print(a == b)           #False       
print(a != b)           #True
print(a > b)            #True
print(a < b)            #False
print(a >= b)           #True
print(a <= b)           #False


3. Logical Operators(and, or , not): Logical operators are used to combine or reverse conditions. They return a Boolean result (True or False). 

age = 20
has_id = True

print(age >= 18 and has_id)     #True
print(age >= 18 or has_id)      #True
print(not has_id)               #False


4. Assignment Operators(=, +=, -=, /=, *=, %=, //=, **=):Assignment operators are used to assign values to variables and update their values.

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24


5. Membership Operators: Membership operators are used to check whether a value exists in a sequence, such as a string, list or tuple.

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)       # True
print("Orange" in fruits)      # False
print("Orange" not in fruits)  # True


6. Identity Operators: Identity operators are used to check whether two variables refer to the same object in memory.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True


7. Bitwise Operators: Bitwise operators are used to perform operations on the binary (0s and 1s) representation of numbers.

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

"""
