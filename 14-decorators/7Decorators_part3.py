#usr/bin/windows/python
from functools import wraps

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """ This is wrapper Function """
        print("This is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def func(a):
    print(f"This is a function with argument {a}")
func(3)

@decorator_function
def func1(a,b):
    """ This is add function """
    return a+b
print(func1(2,9))
print(func1.__doc__)
print(func1.__name__)