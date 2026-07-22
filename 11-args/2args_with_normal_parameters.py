#args_with_normal_parameters

def Multiply(num, *args): #function
    Multiply = 1 # multiply var, not 0 should be 1
    print(args)
    for i in args:
        Multiply *= i
    return Multiply
print(Multiply(2,3,4,6))
# aik zaruri baat normal parameter *args k bad nahi likhna chahiye