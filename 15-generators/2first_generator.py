# create your first generator with generator function
# 1) Generator function
# 2) Generator comprehension

def num(n):
    for i in range(1,n+1):
        yield(i)
numbers = num(10)
for j in numbers:
    print(j)
# yield is a keyword