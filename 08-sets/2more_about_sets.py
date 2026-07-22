# in-keyword and for loop in sets

# inkeyword
s = {'a', 'b', 'c'}
if 'b' in s:
    print("present")
else:
    print("Nope")

# for loop
for items in s:
    print(items)

# set maths
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

#union
#intersection

# do set me se jo  usko combine karna (union)

#union_set = s1 | s2
#print(union_set)

# jo dono me common ho (intersection)

print(s1 & s2)  # we use & for intersection