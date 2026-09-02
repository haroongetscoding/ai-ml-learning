"""
=============================================================
 PYTHON BASICS - COMPLETE GUIDE FOR AI/ML BEGINNERS
=============================================================
 Author: Haroon Abdullah
 Repository: ai-ml-learning
 GitHub: https://github.com/haroongetscoding/ai-ml-learning
 
 This guide covers ALL fundamental Python concepts you need
 to kickstart your AI/ML journey.
=============================================================
"""

# ============================================================
# SECTION 1: PRINTING & COMMENTS
# ============================================================

# Single line comment
"""
Multi-line comment / docstring
"""

print("Hello, AI World!")
print("Welcome to Python Basics")

# Print multiple values
print("Name:", "Haroon", "| Age:", 25)

# Print with formatting
print("=" * 50)


# ============================================================
# SECTION 2: VARIABLES & DATA TYPES
# ============================================================

print("\n--- SECTION 2: VARIABLES & DATA TYPES ---\n")

# String
name = "Haroon"
print(f"Name: {name} (Type: {type(name)})")

# Integer
age = 25
print(f"Age: {age} (Type: {type(age)})")

# Float
cgpa = 3.85
print(f"CGPA: {cgpa} (Type: {type(cgpa)})")

# Boolean
is_student = True
print(f"Is Student: {is_student} (Type: {type(is_student)})")

# None type
nothing = None
print(f"Nothing: {nothing} (Type: {type(nothing)})")


# ============================================================
# SECTION 3: STRING OPERATIONS
# ============================================================

print("\n--- SECTION 3: STRING OPERATIONS ---\n")

first_name = "Haroon"
last_name = "Abdullah"

# Concatenation
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# String methods
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Length: {len(full_name)}")
print(f"Replace: {full_name.replace('Haroon', 'Ali')}")
print(f"Split: {full_name.split(' ')}")
print(f"Starts with Haroon: {full_name.startswith('Haroon')}")
print(f"Contains Abdullah: {'Abdullah' in full_name}")

# String indexing
print(f"First character: {first_name[0]}")
print(f"Last character: {first_name[-1]}")
print(f"Slice [0:3]: {first_name[0:3]}")

# f-strings (formatted string literals) - PREFERRED METHOD
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")


# ============================================================
# SECTION 4: TYPE CONVERSION / CASTING
# ============================================================

print("\n--- SECTION 4: TYPE CONVERSION ---\n")

# String to Integer
age_str = "25"
age_num = int(age_str)
print(f"String to Int: {age_num} (Type: {type(age_num)})")

# Integer to String
price = 100
price_str = str(price)
print(f"Int to String: {price_str} (Type: {type(price_str)})")

# Integer to Float
temp = int(36.5)
print(f"Float to Int: {temp}")

# Float to Integer
marks = float(85)
print(f"Int to Float: {marks}")

# Input always returns string - must convert
# Uncomment the lines below to test interactively:
# user_age = int(input("Enter your age: "))
# print(f"You are {user_age} years old!")
print("Input example: user_age = int(input('Enter age: '))")


# ============================================================
# SECTION 5: ARITHMETIC OPERATORS
# ============================================================

print("\n--- SECTION 5: ARITHMETIC OPERATORS ---\n")

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Power (a ** b): {a ** b}")


# ============================================================
# SECTION 6: COMPARISON & LOGICAL OPERATORS
# ============================================================

print("\n--- SECTION 6: COMPARISON & LOGICAL OPERATORS ---\n")

x = 10
y = 20

# Comparison operators
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# Logical operators
a_val = True
b_val = False
print(f"True AND False: {a_val and b_val}")
print(f"True OR False: {a_val or b_val}")
print(f"NOT True: {not a_val}")


# ============================================================
# SECTION 7: CONDITIONAL STATEMENTS
# ============================================================

print("\n--- SECTION 7: CONDITIONAL STATEMENTS ---\n")

# if-elif-else
score = 75

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# Nested if
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("Need ID proof")
else:
    print("Too young for entry")

# Ternary operator (one-liner if-else)
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")


# ============================================================
# SECTION 8: LOOPS
# ============================================================

print("\n--- SECTION 8: LOOPS ---\n")

# For loop - range
print("For loop (range 1-5):")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

# For loop - list
print("For loop (list):")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"  {fruit}")

# For loop - enumerate
print("For loop (enumerate):")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# While loop
print("While loop (countdown):")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Launch!")

# Loop control - break
print("Break example:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end=" ")
print()

# Loop control - continue
print("Continue example (skip 3):")
for i in range(1, 8):
    if i == 3:
        continue
    print(f"  {i}", end=" ")
print()

# Nested loops
print("Multiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i*j:2d}", end=" ")
    print()


# ============================================================
# SECTION 9: LISTS
# ============================================================

print("\n--- SECTION 9: LISTS ---\n")

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# Accessing elements
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice [1:3]: {numbers[1:3]}")

# Modifying lists
numbers.append(6)            # Add to end
numbers.insert(0, 0)        # Insert at index
numbers.extend([7, 8])      # Add multiple elements
print(f"After append/insert/extend: {numbers}")

# Removing elements
numbers.remove(3)            # Remove by value
popped = numbers.pop()      # Remove last element
del numbers[0]               # Remove by index
print(f"After removals: {numbers}")
print(f"Popped value: {popped}")

# List methods
print(f"Length: {len(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Count of 5: {numbers.count(5)}")

# Sorting
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens: {evens}")


# ============================================================
# SECTION 10: TUPLES
# ============================================================

print("\n--- SECTION 10: TUPLES ---\n")

# Tuples are IMMUTABLE (cannot be changed)
coordinates = (10, 20)
colors = ("red", "green", "blue")

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")

# Accessing
print(f"X: {coordinates[0]}")
print(f"First color: {colors[0]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# When to use tuples over lists?
# - Tuples are faster
# - Tuples are immutable (safer for constants)
# - Tuples can be dictionary keys


# ============================================================
# SECTION 11: DICTIONARIES
# ============================================================

print("\n--- SECTION 11: DICTIONARIES ---\n")

# Creating dictionaries
student = {
    "name": "Haroon",
    "age": 25,
    "cgpa": 3.85,
    "courses": ["AI", "ML", "Python"]
}

print(f"Student: {student}")

# Accessing values
print(f"Name: {student['name']}")
print(f"Safe access: {student.get('phone', 'N/A')}")

# Modifying dictionaries
student["age"] = 26
student["email"] = "haroon@email.com"
print(f"Updated: {student}")

# Removing elements
del student["email"]
popped_val = student.pop("cgpa")
print(f"After removal: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Iterating through dictionaries
print("Iterating:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Nested dictionaries
school = {
    "student1": {"name": "Haroon", "grade": "A"},
    "student2": {"name": "Ali", "grade": "B"}
}
print(f"Nested: {school}")


# ============================================================
# SECTION 12: SETS
# ============================================================

print("\n--- SECTION 12: SETS ---\n")

# Sets are UNORDERED and UNIQUE
numbers_set = {1, 2, 3, 4, 5}
print(f"Set: {numbers_set}")

# Remove duplicates
list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique = set(list_with_dupes)
print(f"Unique values: {unique}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference (A-B): {set_a - set_b}")
print(f"Symmetric Difference: {set_a ^ set_b}")

# Set methods
set_a.add(6)
set_a.remove(1)
print(f"After add/remove: {set_a}")


# ============================================================
# SECTION 13: FUNCTIONS
# ============================================================

print("\n--- SECTION 13: FUNCTIONS ---\n")

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Haroon"))

# Default parameters
def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_with_default("Haroon"))
print(greet_with_default("Haroon", "Good Morning"))

# *args and **kwargs
def flexible_func(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_func(1, 2, 3, name="Haroon", age=25)

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"Add 3+7: {add(3, 7)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")


# ============================================================
# SECTION 14: LIST COMPREHENSIONS (DEEPER)
# ============================================================

print("\n--- SECTION 14: LIST COMPREHENSIONS ---\n")

# Basic
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Dict comprehension
word = "hello"
char_count = {char: word.count(char) for char in set(word)}
print(f"Char count: {char_count}")

# Set comprehension
unique_lengths = {len(word) for word in ["hello", "world", "python", "ai"]}
print(f"Unique lengths: {unique_lengths}")


# ============================================================
# SECTION 15: FILE HANDLING
# ============================================================

print("\n--- SECTION 15: FILE HANDLING ---\n")

# Writing to file
with open("sample.txt", "w") as file:
    file.write("Hello, AI World!\n")
    file.write("This is a test file.\n")
    file.write("Line 3 of the file.\n")

print("File created successfully!")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()
    print(f"File content:\n{content}")

# Reading line by line
with open("sample.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# Appending to file
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

# Check if file exists
import os
if os.path.exists("sample.txt"):
    print(f"File size: {os.path.getsize('sample.txt')} bytes")

# Cleanup
os.remove("sample.txt")
print("File removed!")


# ============================================================
# SECTION 16: ERROR HANDLING (EXCEPTIONS)
# ============================================================

print("\n--- SECTION 16: ERROR HANDLING ---\n")

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion!")
except TypeError:
    print("Type error!")

# Try-except-else-finally
try:
    value = 42
    result = value / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")  # Runs if no exception
finally:
    print("This always runs!")  # Always runs

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount}. Balance: ${balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")


# ============================================================
# SECTION 17: OOP - CLASSES & OBJECTS
# ============================================================

print("\n--- SECTION 17: OOP - CLASSES & OBJECTS ---\n")

class Student:
    # Class variable
    school = "AI Academy"
    
    def __init__(self, name, age, cgpa):
        # Instance variables
        self.name = name
        self.age = age
        self.cgpa = cgpa
    
    # Instance method
    def get_info(self):
        return f"{self.name}, Age: {self.age}, CGPA: {self.cgpa}"
    
    # String representation
    def __str__(self):
        return f"Student({self.name})"
    
    # Class method
    @classmethod
    def from_string(cls, student_str):
        name, age, cgpa = student_str.split("-")
        return cls(name, int(age), float(cgpa))
    
    # Static method
    @staticmethod
    def is_valid_cgpa(cgpa):
        return 0.0 <= cgpa <= 4.0

# Creating objects
student1 = Student("Haroon", 25, 3.85)
student2 = Student("Ali", 23, 3.72)

print(student1.get_info())
print(student2.get_info())
print(f"School: {Student.school}")

# Class method usage
student3 = Student.from_string("Sara-22-3.95")
print(student3.get_info())

# Static method usage
print(f"Valid CGPA: {Student.is_valid_cgpa(3.85)}")


# ============================================================
# SECTION 18: INHERITANCE
# ============================================================

print("\n--- SECTION 18: INHERITANCE ---\n")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")
        self.breed = breed
    
    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, sound="Meow")
        self.color = color
    
    def purr(self):
        return f"{self.name} purrs..."

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.speak())
print(dog.fetch())
print(cat.speak())
print(cat.purr())

# Polymorphism
animals = [Dog("Rex", "German Shepherd"), Cat("Luna", "Black")]
for animal in animals:
    print(animal.speak())


# ============================================================
# SECTION 19: MODULES & PACKAGES
# ============================================================

print("\n--- SECTION 19: MODULES & PACKAGES ---\n")

# Importing modules
import math
import random
from datetime import datetime

# Math module
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceil 4.3: {math.ceil(4.3)}")
print(f"Floor 4.7: {math.floor(4.7)}")

# Random module
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['a', 'b', 'c'])}")

# DateTime
now = datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


# ============================================================
# SECTION 20: DECORATORS
# ============================================================

print("\n--- SECTION 20: DECORATORS ---\n")

import time

# Simple decorator
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    return "Done!"

result = slow_function()
print(result)


# ============================================================
# SECTION 21: GENERATORS
# ============================================================

print("\n--- SECTION 21: GENERATORS ---\n")

# Generator function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using generator
print("Fibonacci sequence:")
for num in fibonacci(10):
    print(f"  {num}", end=" ")
print()

# Generator expression
squares_gen = (x**2 for x in range(10))
print(f"Squares generator: {list(squares_gen)}")


# ============================================================
# SECTION 22: LIST/SET/DICT COMPREHENSIONS SUMMARY
# ============================================================

print("\n--- SECTION 22: COMPREHENSIONS SUMMARY ---\n")

# List comprehension
list_comp = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
dict_comp = {x: x**2 for x in range(5)}

# Set comprehension
set_comp = {x for x in range(10) if x % 3 == 0}

# Generator expression
gen_comp = (x**2 for x in range(10))

print(f"List: {list_comp}")
print(f"Dict: {dict_comp}")
print(f"Set: {set_comp}")
print(f"Generator: {list(gen_comp)}")


# ============================================================
# SECTION 23: PRACTICAL EXAMPLE - AI/ML PREVIEW
# ============================================================

print("\n--- SECTION 23: AI/ML PREVIEW ---\n")

import math

# Simple linear regression (no libraries)
def simple_linear_regression(x_values, y_values):
    n = len(x_values)
    
    # Calculate means
    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n
    
    # Calculate slope (m) and intercept (b)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    
    m = numerator / denominator
    b = y_mean - m * x_mean
    
    return m, b

# Example data: Study hours vs Exam scores
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [45, 55, 65, 75, 80, 85, 90, 95]

slope, intercept = simple_linear_regression(hours, scores)
print(f"Linear Regression Model:")
print(f"  Slope: {slope:.2f}")
print(f"  Intercept: {intercept:.2f}")
print(f"  Formula: y = {slope:.2f}x + {intercept:.2f}")

# Predict score for 10 hours study
predicted = slope * 10 + intercept
print(f"  Predicted score for 10 hours: {predicted:.2f}")

# Calculate R-squared
y_mean = sum(scores) / len(scores)
ss_total = sum((y - y_mean) ** 2 for y in scores)
ss_residual = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(hours, scores))
r_squared = 1 - (ss_residual / ss_total)
print(f"  R-squared: {r_squared:.4f}")


# ============================================================
# SECTION 24: USEFUL TIPS & TRICKS
# ============================================================

print("\n--- SECTION 24: USEFUL TIPS & TRICKS ---\n")

# Swap variables
a, b = 5, 10
a, b = b, a
print(f"Swapped: a={a}, b={b}")

# Multiple assignment
x = y = z = 0
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Unpacking
coords = (1, 2, 3)
x, y, z = coords
print(f"Unpacked: x={x}, y={y}, z={z}")

# Dictionary from two lists
keys = ["name", "age", "city"]
values = ["Haroon", 25, "Karachi"]
dict_from_lists = dict(zip(keys, values))
print(f"Dict from lists: {dict_from_lists}")

# Check membership
print(f"'python' in 'python basics': {'python' in 'python basics'}")
print(f"3 in [1, 2, 3]: {3 in [1, 2, 3]}")

# Walrus operator (Python 3.8+)
numbers = [1, 5, 12, 3, 18, 7]
if (n := max(numbers)) > 10:
    print(f"Max is {n}, which is > 10")


# ============================================================
# SECTION 25: COMPLETE PROGRAM - STUDENT MANAGEMENT
# ============================================================

print("\n--- SECTION 25: COMPLETE PROGRAM ---\n")

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, age, cgpa):
        student = {"name": name, "age": age, "cgpa": cgpa}
        self.students.append(student)
        print(f"Added: {name}")
    
    def display_all(self):
        if not self.students:
            print("No students found!")
            return
        
        print("\n--- All Students ---")
        for i, s in enumerate(self.students, 1):
            print(f"{i}. {s['name']} | Age: {s['age']} | CGPA: {s['cgpa']}")
    
    def search_student(self, name):
        found = [s for s in self.students if s['name'].lower() == name.lower()]
        if found:
            for s in found:
                print(f"Found: {s['name']} | Age: {s['age']} | CGPA: {s['cgpa']}")
        else:
            print(f"Student '{name}' not found!")
    
    def average_cgpa(self):
        if not self.students:
            return 0
        return sum(s['cgpa'] for s in self.students) / len(self.students)

# Demo
manager = StudentManager()
manager.add_student("Haroon", 25, 3.85)
manager.add_student("Ali", 23, 3.72)
manager.add_student("Sara", 22, 3.95)
manager.display_all()
manager.search_student("Ali")
print(f"\nAverage CGPA: {manager.average_cgpa():.2f}")


# ============================================================
# CONGRATULATIONS! You've completed Python Basics!
# ============================================================

print("\n" + "=" * 60)
print(" CONGRATULATIONS!")
print(" You've completed Python Basics!")
print(" You're now ready for AI/ML!")
print("=" * 60)
print("\n Next Steps:")
print("  1. Learn NumPy & Pandas")
print("  2. Study Matplotlib & Seaborn")
print("  3. Explore Scikit-learn")
print("  4. Dive into TensorFlow/PyTorch")
print("\n GitHub: https://github.com/haroongetscoding/ai-ml-learning")
print("=" * 60)
