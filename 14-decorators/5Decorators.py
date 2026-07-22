# Decorators -- > enhance the functionality of other functions

# decorator aik function hi hai jo humare function ko enhance karti hai
# this is awesome function
def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function
# @decorator_function # shortcut
def func1():
    print('this is function one')
# func1()
def func2():
    print('this is function two')

var = decorator_function(func1) # yahan var ki jaga func1 b likh sakte
var()

# syntastic suggur ---> @ use to enhance decorator's code