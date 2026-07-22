#function with all type  of parameters
# very important to understand

# PADK
# parameters,,, normal
# args
# default parameters
# kwargs **

# important ===> PADK
def func(name, *args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Hamza', 1,2,3, b = 1, a = 2)
# order maintance rakhna zaruri hai