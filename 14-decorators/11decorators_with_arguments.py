from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(args) == (data_type) for arg in  args]):
                return function(*args, **kwargs)
            print("Invalid Arguments")
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_concatenate(*args):
    string_variable = ""
    for i in args:
        string_variable += i
        return string_variable
print(string_concatenate('hamza','baloch'))