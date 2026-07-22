# lambda Expression   (anonymous function)

# unique topic of python3
# what is lambda expression
# lambda expression is a function that can be define in single line

# define a normal function
def add(a,b):
    return a+b


# define a lambda function
lambda a,b : a+b

"""how to use
we can store it in a variable
remember:- we do not store lambda in a variable (we can but we shouldn't)
we use lambda with builtin functions
map, reduce, filter"""

multiply = lambda a,b : a*b
print(multiply(2,3))