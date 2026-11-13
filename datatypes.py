"""Datatypes in Python: It denotes the type of data that a variable can hold. Python has several built-in datatypes, including:
1. Numeric Types: int, float, complex
2. Sequence Types: list, tuple, range
3. Text Type: str
4. Set Types: set, frozenset
5. Mapping Type: dict
6. Boolean Type: bool
7. Binary Types: bytes, bytearray, memoryview
"""

a = 10  # int
b = 3.14  # float
c = 2 + 3j  # complex
d = [1, 2, 3]  # list
e = (1, 2, 3)  # tuple
f = range(5)  # range
g = "Hello, World!"  # str
h = {1, 2, 3}  # set
i = frozenset([1, 2, 3])  # frozenset
j = {"name": "Alice", "age": 25}  # dict
k = True  # bool
l = b"Hello"  # bytes
m = bytearray(b"Hello")  # bytearray
n = memoryview(b"Hello")  # memoryview
o = None  # NoneType
p = (1, "two", 3.0)  # tuple with mixed types
q = [1, "two", 3.0]  # list with mixed types
r = {1, "two", 3.0}  # set with mixed types
s = {"one": 1, "two": 2.0, "three": "3"}  # dict with mixed types


#Difference between set and frozen set

"""
In Python, both set and frozenset are built-in data structures used to store unordered collections of unique, hashable elements. The primary difference between them is mutability: a set can be modified after creation, while a frozenset is immutable. This means that you can add or remove elements from a set, but you cannot do so with a frozenset.

Syntax:
a = set([1, 2, 3]) or {1,2,3}  # Creating a set
b = frozenset([1, 2, 3])  # Creating a frozenset

"""