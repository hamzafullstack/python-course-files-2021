# Last exercise solution 
def sublister(l):
    count = []
    for i in l:
        if type(i) == list:
            count += 1
    return count
mixed = [1,2,3,4]
print(sublister(mixed))