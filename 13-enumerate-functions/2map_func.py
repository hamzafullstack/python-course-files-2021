# map Function

# map func with lambda expression
numbers = [1,2,3,4]
squares = list(map(lambda a:a**2, numbers))
print(squares)

"""yeh kam normaly be kar sakte hain 
aur list comp se be
aik problem k different solutions be ho sakte hain"""

# list comp 
square_list = [i**2 for i in numbers]
print(square_list)

"""
pre defined functions me Lambda expression use karni chahiye for quick coding
"""
