# more about tuples

# loop in tuples
numbers = (1,2,3,4,5)
# for i in numbers:
#     print(i)
#NOTE - We can also use while loop too 

#tuples with one elements/
num = (1,) # use comma seprated
word = ("word1",) # use comma seprated

# tuples without parenthesis
lang = 'C++', 'python', 'java', 'php'
#print(type(lang))

# Tuples Unpacking
Languages = ('python', 'java', 'cpp', 'php','kotlin')
Language1, Language2, Language3, Language4, Language5 = (Languages)
#print(Language1)


# list inside tuples
fav = ('karachi Pakistan', ["Layari", "clafton SeaView", "saddar"]) #list in tuple
fav[1].pop()
fav[1].append("Gulshan-E-Hadeed")
print(fav)

# some functions that we can use in tuples

# min (),
# max (),
# sum,