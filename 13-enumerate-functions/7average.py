# define a function take any number of lists containing numbers

# Try to  make it anonymous function using lambda expressions
Average = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(Average([1,2,3], [4,5,6], [7,8,9]))