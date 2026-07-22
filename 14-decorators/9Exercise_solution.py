# define a Decorator that calculate time
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(f" executing {function.__name__}")
        time_one = time.time()
        function(*args, **kwargs)
        returned_value = function(*args, **kwargs)
        time_two = time.time()
        total_time = time_one - time_two
        print(f"This function took {total_time} seconds")
        return returned_value
    return wrapper_function
# defining a function that retun a square of list "i use list comprehension"
@calculate_time
def square_finder(number):
    return [i**2 for i in range(1,number+1)]
square_finder(1000)