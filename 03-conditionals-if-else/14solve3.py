name = input("enter your name : ") # user input
# Ameerhamza etc
temp_variable = ""  #empty
i = 0
while i < len(name):
    if name [i] not in temp_variable:
        temp_variable += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        i += 1