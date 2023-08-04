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
