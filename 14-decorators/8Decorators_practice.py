#usr/bin/windows/python
from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__} Function")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def adding(a,b):
    """ This function takes two numbers as argument and return their sum """
    return a + b
print(adding(2,3))