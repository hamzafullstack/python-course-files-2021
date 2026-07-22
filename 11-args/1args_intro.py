# Make Flexible functions

# *operater
# *args

# agar marzi mutabik arguments pass karane hain function mai to use *args
#def all_total(*args):
#    #print(args)
#all_total(12,3,4,5,77)
# remember:- Args hamesha tuples me leta arguments
# remember:- *args likhna convension hai rule nahi

#      for loop in args =======Total=== sum 

def test(*args):
    total = 0
    for num in args:
        total += num
    return total
# print(test(1,2,3))
# jitne marzi arguments pass karvaeen