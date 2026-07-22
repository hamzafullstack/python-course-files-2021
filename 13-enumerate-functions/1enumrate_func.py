# enumerate Function
# we use enumerate function with for loop to track position  of our item in  iterable

# how can we do this wihout enumerate function????

# names = ['Ali', 'kashi', 'hamza', 'zahid']
# pos = 0
# for name in names:
#     print(f'{pos} --> {name}')
#     pos += 1

# with enumerate function

# names = ['Ali', 'Hamza', 'kashif', 'Zahid']
# for pos, name in enumerate(names):
#     print(f"{pos} ===> {names}")



# Define a function that get two arguments

names_list = ['ALi', 'Ahmed', 'Abdul Sattar', 'Hamza']
def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1
print(find_pos(names_list, 'ALi'))