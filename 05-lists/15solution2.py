# exercise two solution
# def reverse_list(l):
#     l.reverse()
#     return l

# hum aise be kar sakte hain

# aur aise be
# def reverse_list(l):
#     return l[::-1]
# same we used in string slicing..
#============- NEXT -================
def reverse_list(l):
    l_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        l_list.append(popped_item)
    return l_list
numbers = [1,2,3,4,5]
print(reverse_list(numbers))