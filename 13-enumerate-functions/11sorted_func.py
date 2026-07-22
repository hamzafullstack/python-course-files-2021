# Advance Sorted function

# hum ne list me parha tha sorted method k baare mai
fruits = ['grapes', 'Mango', 'Banana', 'Apple']
# as we used sort method in list

fruits2 = ('grapes', 'Mango', 'Banana', 'Apple')
sorted(fruits2)
print(fruits2)
# remember:- yeh phir be sorted list me karega

fruits3 = {'grapes', 'Mango', 'Banana', 'Apple'} #sets
print(sorted(fruits3))

#now lets Talk about some advance data structures
guitars = [
    {'model' : 'Yamaha f310', 'price' : 8400},
    {'model' : 'faith napture', 'price' : 500000}
]
print(sorted(guitars, key = lambda d :d.get('price')))
# print(sorted(guitars, key = lambda d :d['price']))
#print(sorted(guitars, key = lambda d :d['price'], reverse = True)) #reverse
guitars_test = print(sorted(guitars, key = lambda d :d['price'], reverse = True))