# pass Function as a argument

# make own function that take function as a argument
def square(a):
    return a**2
list_test = [1,2,3,4]
def my_func(fuck, list_test):
    new_list = []
    for i in list_test:
        new_list.append(fuck(i))
    return new_list