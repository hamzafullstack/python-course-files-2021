"""
Generate list with Range Function
something more about pop method
index method
pass list to a function
"""

# Generate a list using range function
# number = list(range(1,11))
# print(number)
# range function k sath list create karna


# pop method
num = [1,2,3,4,5]
num.pop()
#print(num)
#actualy pop method humhe value return be karta jo delete karta ye
# like this
#print(num.pop())


#index method
#print(num.index(3)) #(3, 11, 17))


#pass list a in function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))