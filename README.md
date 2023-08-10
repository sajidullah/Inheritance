# Python Decorators Example

This repository contains a simple example of using decorators in Python. Decorators are a powerful feature in Python that allow you to modify or extend the behavior of functions or methods without changing their code directly.

## What is a Decorator?

A decorator is a function that takes another function as input and extends or modifies its behavior. It is commonly used to perform actions before and/or after the execution of the target function. Decorators are often used for tasks like logging, authentication, or code instrumentation.

## Example

In this example, we define a decorator `my_decorator` that adds a pre- and post-processing step around a target function. We apply this decorator to the `say_hello` function, which prints a simple greeting.

```python
# Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Use the decorator
@my_decorator
def say_hello():
    print("Hello, decorator!")

# Call the decorated function
say_hello()
# Inheritance
