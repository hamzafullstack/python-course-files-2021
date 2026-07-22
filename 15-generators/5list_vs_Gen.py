import time
""" list VS Generators """
""" Memory usage, Time """
#  when to use  lists and when to use Generators
t1 = time.time
list_comp =[i**2 for i in range(10000000)] # 10million
print(time.time() - t1)
#Generator_comp = (i**2 for i in range(10000000)) # 10million