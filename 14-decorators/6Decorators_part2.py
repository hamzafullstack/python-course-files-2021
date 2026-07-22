def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def func(a):
    print(f"This is a function with argument {a}")
func(3)

@decorator_function
def func1(a,b):
    return a+b
print(func1(2,9))
# always use return in decorators and also in functions