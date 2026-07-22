"""what is Lists comprehension????
with the help of list comprehension we can create list in one line"""

# list comprehension
# create a lists Comp square of 10 numbers
square = [i**2 for i in range(1,11)]
print(square)

# negative
negative = [-1 for i in range(1,11)]
print(negative)

"""shuru me yeh dekhna hai k append kya karna hai"""

# list comp as normal 
data = ['Ameerhamza', 'Kashif', 'zahid']
print(data)

data1 = [data[0] for i in data]
print(data1)