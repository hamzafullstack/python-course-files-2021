# exercise 3 solution
def reverse_element(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words = ['abc', 'kam', 'iam']
print(reverse_element(words))
# simple