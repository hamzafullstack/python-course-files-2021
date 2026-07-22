# generator comprehension 

# for example "List COmp"
square = [i**2 for i in range(1,11)]
print(square)

# gen comp
square = (i**2 for i in range(1,11))
for num in square:
    print(num)