# exercise 5 solution
# common elements finder function

#function
def common_finder(l1, l2):
    output = []
    for i in l1:
        for i in l2:
            output.append(i)
    return output

print(common_finder([1,2,5,4], [2,8,7]))