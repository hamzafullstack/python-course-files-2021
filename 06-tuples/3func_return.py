# Function return two values
def func(int1, int2):
    add = int1 + int2
    multiply = int1*int2
    return add, multiply
#print(func(4,7))
# jab be 2 values returns karvaengy woh tuples me return dega
add, multiply = func(3,8)
print(add)
print(multiply)
