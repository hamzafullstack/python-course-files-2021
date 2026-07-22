# args as a argument

def multiply(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *= i
    return multiply
num = (2,4,6)
print(multiply(*num)) #  unpack lists and tuples
# use * and parameter