
# Object-Oriented Programming (OOP) Project

# Description
This project demonstrates the principles of Object-Oriented Programming (OOP) using Python. It covers class creation, constructors, method definitions, and inheritance.

# Features
- Creation of classes and objects
- Implementation of parent and child classes
- Use of `super()` to call parent class methods
- Instance methods and attributes
- Demonstration of inheritance and method overriding

# Definitions
- "Class": A blueprint for creating objects that encapsulate data and behavior.
- Object: An instance of a class containing specific data.
- Constructor (`__init__` method): A special method that initializes an object's attributes.
- Method: A function defined inside a class that operates on instances.
- Inheritance: A mechanism where a child class acquires properties and behavior from a parent class.
- `super()`: A function used to call methods from the parent class within a child class.

# Code Overview
# Class Creation
A class in Python is created using the `class` keyword. Below is an example:
```python
class Human:
    pass
```

# Parent Class: `Human`
This class includes a constructor and a method to display information.
```python
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        print(f"Hey, my name is {self.name}, I'm {self.gender}, and I'm {self.age} years old.")
```

# Child Class: `Boy`
The `Boy` class inherits from `Human` and adds an additional attribute, `schoolname`.
```python
class Boy(Human):
    def __init__(self, name, age, gender, schoolname):
        super().__init__(name, age, gender)
        self.schoolname = schoolname
    
    def school(self):
        print(f"I study at {self.schoolname}.")
```

# Creating Objects and Using Methods
```python
b = Boy("James", 15, "male", "UTAMU")
b.info()
b.school()
```

# Expected Output
```
Hey, my name is James, I'm male, and I'm 15 years old.
I study at UTAMU.
```

# Technologies Used
- Python

# Author
[Atuhaire abiudi](https://github.com/22atuhaire)

# License
This project is licensed under GNU GENERAL PUBLIC LICENSE License.

