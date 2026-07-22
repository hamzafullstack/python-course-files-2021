# function returning function (closure Practice)
# closure:- first class function
def to_power(x): # x = 3
    def calc_power(n): # n = 2
        return n**x
    return calc_power

cube = to_power(3)
print(cube(2))