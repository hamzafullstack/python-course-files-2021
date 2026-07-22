# Exercise One solution

def to_power(num, *args):
    if args:
        return [i**num for i in args] #list comp
    else:
        return "you didn't pass any args"

num = [1,2,3,4]
print(to_power(3, *num)) # *[1,2,3,4]