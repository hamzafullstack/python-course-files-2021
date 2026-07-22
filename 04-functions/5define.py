# define a greatest value counter function
def greatest(a,b,c):
    if a>b and a>c: #statements
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(30,34,40))