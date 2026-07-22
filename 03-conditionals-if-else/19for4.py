#  For Loop example part 3
# get user input and count characters inside it

name = input("Enter your name : ")
temp = ""
for i in range(len(name)):
    if name [i] not in temp:
        print(f"{name [i]}: {name.count(name[i])}")
        temp += name[i]