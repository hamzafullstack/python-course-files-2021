# intro to sets
#
"""sets:- unordered collection of unique items"""

# How to make a set
s = {1,2,3,4,5,5,3,4,1,1,1}
print(s)

# sirf unique items hi print hongy
# print(s[1]) # error
# no indexing in sets

# remove duplicates
# use Set function
l = [1,2,3,4,4,4,5,5,5,6,7,8,9,9]
# l is a lists
""" wanna use set function to change it into sets and remove duplicates """
#s2 = set(l)
#print(s2)

# important use of sets(list+set)

#s2 = list(set(l))
#print(s2)

"""methods for sets"""

# Add Method
s3 = {1,2,3}
#s3.add(4)
#print(s3)


# Remove method
#s3.remove(2)
#print(s3)

# discard method (Good)
s3.discard(5)
print(s3)
# discard method same remove method jesi hai


#clear method
#s3.clear()
#print(s3)

# copy method
#s4 = s3.copy()

#hum sets me dictionaries tuples and lists store nhi kara sakte hain