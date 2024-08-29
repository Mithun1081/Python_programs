"""
In Python, an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. When an exceptional situation arises that the code cannot handle, Python raises an exception. This could be due to various reasons such as incorrect user input, unexpected conditions, or errors in the program logic.

When an exception occurs, Python stops executing the normal flow of the program and looks for an exception handling mechanism. If the exception is not caught and handled properly, the program will terminate abruptly, and an error message will be displayed, indicating the type of exception that occurred along with a traceback, which shows the sequence of function calls that led to the exception.

Python provides a structured way to handle exceptions using the `try`, `except`, `else`, and `finally` blocks:

- `try`: This block contains the code that might raise an exception.
- `except`: This block catches and handles the exceptions raised in the `try` block.
- `else`: This block executes if no exceptions are raised in the `try` block.
- `finally`: This block executes regardless of whether an exception occurred or not, and is generally used for cleanup actions.

Here's a simple example:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception (division by zero)
    print("Error: Division by zero!")
else:
    # Executed if no exception occurred
    print("Division successful!")
finally:
    # Cleanup or final actions, executed regardless of exceptions
    print("Exiting the try-except block.")
```

In this example, if a division by zero occurs, the `ZeroDivisionError` exception is caught and handled in the `except` block. If no exception occurs, the `else` block is executed. Finally, the `finally` block is always executed, regardless of whether an exception occurred or not.
"""



a=int(input("enter the number1"))
b=int(input("enter the number2"))
try:
    c=a/b
except ZeroDivisionError:
    print("This is my first error")
else:
    print("hello world")

print()
""""""
x=5
y="hello"
try:
    z=x+y
except TypeError:
    print("Error: cannot add an int and a str")
print()

""""""
def fun(a):
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")