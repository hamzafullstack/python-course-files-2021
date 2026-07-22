# exercise one Solution
def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name [::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ['AmeerHamza', 'kashif']
print(func(names)) # , reverse_str = True) 
# remember **kwargs is an optional argument