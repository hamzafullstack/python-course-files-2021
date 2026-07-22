"""Delete data from List
Common methods used to delete data from list
1st and common method >>>>  "pop method"""
fruits = ['Mango', "Kiwi", "orange", 'Banana', "Apple"]
#fruits.pop() # agar pop me element pass nahi karengy to by default wo last item
# ko list me se remove kar dega 
#print(fruits)
# for passing element l.pop(1) simple 0 1 2 3 4 5
# delete operater,,, // statement {no matter what is it? heheheh}


# Delete del
# del fruits[1] # code style 
# print(fruits)

# remove method:
# koi particular element mujhe nahi pata mere list me kahan hai aur mujhe remove karna
# to me use kar sakta hun remove method ko,,

#remove Method
fruits.remove("Banana")
print(fruits)

# for adding data to list
# append, extend, insert

#for deleting data from list
# pop, remove, del