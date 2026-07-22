# exercise one solutions


def reverse_str(l):
    return [name[::-1] for name in l] #returning list comp
print(reverse_str(['Hamza', 'Ahmed'])) #argument







# normal way
def reverse_string(a):
    temp = []
    for name in a:
        temp.append(name[::-1])
    return temp