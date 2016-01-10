

"""
The assert keyword is used for debugging purposes. We can use it for testing conditions that are obvious to us.
For example, we have a program that calculates salaries. We know that the salary cannot be less than zero.
So we might put such an assertion to the code. If the assertion fails, the interpreter will complain.
"""

salary = 3500
salary -= 3560 # mistake was done

assert salary > 0
