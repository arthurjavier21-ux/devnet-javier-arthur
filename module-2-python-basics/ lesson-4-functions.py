"""
Module 2 — Lesson 4: Functions
Student: Javier, Arthur
Date: 10/1/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

A function is a block of code na ginawa para gumawa ng isang specific task. Instead na isulat ko ulit yung same code many times, 
pwede kong ilagay yung code inside a function and call it whenever I need it.

============================================
KEY VOCABULARY
============================================
- function: A function is a block of code na ginawa para sa isang specific task.

- def: "def" is used to create or define a function in Python.

- parameter: A parameter is a variable inside the function that can receive a value.

- argument: An argument is the actual value na binibigay natin sa function when we call it.

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
def greet(name):
    print(f"Hello, {name}")

greet("Javier")

def add_numbers(number1, number2):
    return number1 + number2

result = add_numbers(10, 5)

print("The answer is", result)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

print and return
print shows something on the screen, while return gives a value back
from the function. At first, medyo confusing siya for me because
pareho silang may output, pero different yung purpose nila.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
