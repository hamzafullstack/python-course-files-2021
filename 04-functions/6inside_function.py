# Function inside functionb=
# yeh itna aham nahi hai magar ho skta hai future mai zarurat padhe
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

# def new_greatest(a,b,c):
#     bigger = greatest(a,b)
#     return greatest(bigger, c)
# print(new_greatest(30,34,40))

""" there is a principle in programming"""
""" KISS--> Keep It Simple Stupid """