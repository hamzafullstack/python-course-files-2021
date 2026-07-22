# Sets Comprehensions

"""actualy sets comp reall life projects banane mai buhat kam use hota hai"""

s = {k**2 for k in range(1,11)}
print(s)

# another example
names = ['Hamza', 'Kashif','Zahid']
first = {name[0] for name in names}
print(first)