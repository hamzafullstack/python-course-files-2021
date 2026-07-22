# 
def Divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print('Cant divide a number by Zero ')
        print(err)
    except TypeError as err:
        print("Number must be int or floating point ")
print(Divide(10,0))