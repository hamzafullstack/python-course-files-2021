# Function return function
def outer_func():
    """ This is just outer function """
    def inner_func():
        """ this is inner function its inside outer_func """
        print("This is innerfunction, and the outer func return innerfunc")
    return inner_func
var = outer_func()
var()
# humne var me outerfunc ko asign kiya
# an other example
def noobplayer(msg):
    def proplayer():
        print(f"Message is {msg}")
    return proplayer
var_one = noobplayer('hello there ! We are kings')
var_one()