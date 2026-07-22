#  kwargs(keyword arguments)
# **kwargs (The double star operator)
# kwargs me jo be keyword argument pass karengy wo dict input lega
# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} : {v}") # for Loop in kwargs
func(first_name = 'Ameerhamza', last_name = 'Baloch')
# aik baat jo yaad rakhne chahiye woh yeh hai k kwargs hamesha output dict me dekha
# { output }

# dictionaries unpacking
# D = {'name' : 'hamza', 'age' : 20}
#**d