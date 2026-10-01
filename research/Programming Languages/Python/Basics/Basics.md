# Python Basics

## Overview
Python is a high-level, interpreted, general-purpose programming language created by Guido van Rossum in 1991. It emphasizes code readability and simplicity, making it one of the most popular languages for beginners and experts alike. It is widely used in web development, data science, AI/ML, automation, and scientific computing.

## Key Characteristics
- **Paradigm**: Multi-paradigm (procedural, OOP, functional)
- **Typing**: Dynamic, strong, duck typing
- **Execution**: Interpreted (CPython), with optional compilation
- **Memory Management**: Automatic garbage collection
- **Indentation**: Significant whitespace (code blocks defined by indentation)

## Syntax Fundamentals

### Hello World
```python
print("Hello, World!")
```

### Variables and Data Types
```python
# No declaration needed
count = 42              # Integer
price = 19.99           # Float
name = "Alice"          # String
is_active = True        # Boolean
nothing = None          # None (null equivalent)

# Type hints (optional, Python 3.5+)
age: int = 30
greeting: str = "Hello"

# Multiple assignment
x, y, z = 1, 2, 3

# Constants (by convention, uppercase)
MAX_SIZE = 100
```

### Control Flow
```python
# If-elif-else
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Ternary operator
result = "positive" if x > 0 else "non-positive"

# For loop (iterates over sequences)
for i in range(10):
    print(i)

for item in collection:
    print(item)

# For with index
for index, item in enumerate(collection):
    print(index, item)

# While loop
while count > 0:
    count -= 1

# Break and continue
for i in range(10):
    if i == 5:
        break       # Exit loop
    if i % 2 == 0:
        continue    # Skip to next iteration
    print(i)

# Try-except (exception handling)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("Success")
finally:
    print("Always executed")
```

### Functions
```python
# Function definition
def add(a, b):
    return a + b

# Type hints
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# *args and **kwargs
def flexible(*args, **kwargs):
    print(args)    # Tuple of positional args
    print(kwargs)  # Dict of keyword args

# Lambda (anonymous function)
square = lambda x: x ** 2

# Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Data Structures
```python
# List (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(0, "avocado")
fruits.remove("banana")
popped = fruits.pop()
fruits.sort()
fruits.reverse()

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Tuple (immutable, ordered)
point = (3, 7)
x, y = point  # Unpacking

# Set (mutable, unique elements)
unique = {1, 2, 3, 2, 1}  # {1, 2, 3}
unique.add(4)
unique.discard(2)

# Dictionary (key-value pairs)
person = {"name": "Alice", "age": 30}
person["email"] = "alice@example.com"
name = person.get("name", "Unknown")

# Dictionary comprehension
lengths = {name: len(name) for name in fruits}

# Common operations
for key, value in person.items():
    print(key, value)

# Unpacking
first, *rest = [1, 2, 3, 4, 5]
```

### Classes and OOP
```python
class Person:
    # Class variable
    species = "Homo sapiens"

    # Constructor
    def __init__(self, name: str, age: int):
        self.name = name        # Instance variable
        self._age = age         # Protected (convention)

    # Instance method
    def describe(self) -> str:
        return f"{self.name} is {self._age} years old"

    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2025 - birth_year)

    # Static method
    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    # Property
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # Dunder (magic) methods
    def __str__(self):
        return self.describe()

    def __repr__(self):
        return f"Person(name='{self.name}', age={self._age})"

    def __eq__(self, other):
        return self.name == other.name and self._age == other._age

# Inheritance
class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def describe(self):
        return f"{super().describe()} and works at {self.company}"

# Abstract class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    def describe(self):
        return f"Area: {self.area()}"
```

### Modules and Packages
```python
# Import
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import json

# Import with alias
import numpy as np
import pandas as pd

# Relative imports (within packages)
from . import sibling_module
from .. import parent_module

# __name__ == "__main__" guard
if __name__ == "__main__":
    main()
```

### File I/O
```python
# Reading
with open("file.txt", "r") as f:
    content = f.read()
    lines = f.readlines()

# Writing
with open("file.txt", "w") as f:
    f.write("Hello, World!")

# Appending
with open("file.txt", "a") as f:
    f.write("New line\n")

# CSV
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# JSON
import json
data = json.loads(json_string)
json_string = json.dumps(data, indent=2)
```

### Error Handling
```python
# Try-except-else-finally
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except (TypeError, KeyError) as e:
    print(f"Type or key error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No exception raised")
finally:
    print("Cleanup")

# Custom exception
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

# Raise
raise ValidationError("email", "Invalid email format")

# Context manager
class DatabaseConnection:
    def __enter__(self):
        self.conn = create_connection()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

with DatabaseConnection() as conn:
    conn.query("SELECT * FROM users")
```

### Iterators and Generators
```python
# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generator expression
squares = (x**2 for x in range(100))

# Iterator protocol
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current
```

## Common Libraries
- `os`, `sys` — System and OS operations
- `datetime` — Date and time
- `json`, `csv` — Data serialization
- `re` — Regular expressions
- `collections` — Specialized containers
- `itertools`, `functools` — Functional programming
- `pathlib` — File path handling
- `typing` — Type hints
- `unittest`, `pytest` — Testing

## Strengths
- Extremely readable and beginner-friendly
- Massive ecosystem (PyPI has 400k+ packages)
- Excellent for data science, AI/ML, and automation
- Strong community and documentation
- Versatile (web, desktop, mobile, embedded, scientific)

## Weaknesses
- Slower than compiled languages (mitigated by C extensions)
- GIL limits true parallelism in CPython
- Dynamic typing can lead to runtime errors
- Memory consumption higher than lower-level languages
- Mobile and game development support is limited
