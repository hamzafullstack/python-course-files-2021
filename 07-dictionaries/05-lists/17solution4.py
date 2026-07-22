#exercise 4 solution
#filter odd_even Numbers
def filter_odd_even(l):
    odd_nums = []
    even_nums = []
    for i in l:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums, even_nums]
    return output
numbers = [1,2,3,4,5,6,7,8,9]
print(filter_odd_even(numbers))