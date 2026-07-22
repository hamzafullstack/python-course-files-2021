# Filter Function
numbers = [1,2,3,4,7,6,6,5,8,9,10]
evens = filter(lambda a:a%2==0, numbers)
#print(evens)
# for example mai isko tuple nahi karna chahta
for i  in evens:
    print(i)
# filter ko hum  baar baar iterate nahi kar skte hain
# magar tuple and list ko kar sakte hain
# print(filter.__doc__)