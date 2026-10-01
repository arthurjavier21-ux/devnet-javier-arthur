"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Javier, Arthur
Date: 10/1/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]

Control flow is about telling the program kung ano yung dapat niyang
gawin depende sa situation or condition.

============================================
KEY VOCABULARY
============================================
- condition:A condition is something na ccheck ng program. Usually ang result niya is True or False.
- if / elif / else: 
"if" is used kapag may condition tayo na gusto i-check.
"elif" means another condition na i ccheck if the first if is false.
"else" is used kapag wala sa mga previous conditions ang true.
- comparison operator: These are symbols used to compare values, like ==, !=, >, <, >=, and <=.
- boolean expression: A boolean expression is an expression na ang result ay True or False.


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

grade = 85

if grade >= 90:
    print("Excellent!")
elif grade >= 75:
    print("Passed!")
else:
    print("Failed!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
If mag compare ka ng number, instead of equal (=) lang dapat dalawang equal (==) to compare a number. Because using one equal means you are
asigning, while 2 equal means comparing.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
