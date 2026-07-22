"""scope of variables inside and outside of function
scope ko hum use nahi karta magar samjhna important hai
taake future me coding mai ghalatiyan  na karen"""

x = 5 # global variable
def func1():
    global x #global var from scope out
    x = 7 # local variable
    return x
print(x)
print(func1())
print(x)

# function k under global variable ko define karna nahi chahiye