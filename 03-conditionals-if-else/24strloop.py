# # # # for loop in strings:

# # # name = "Ameer Hamza"
# # # for i in range(len(name)):
# # #     print(name[i])
# # # old method jo common hia har programming language me
# # # jese c++ java javascript etc also python me bhi

# # # our yeh new jo sirf python mai hi hain aur buhat hi simple hai
# # name = "Ameer hamza"  #it is a variable---
# # for i in name:  # name humari variable ka nam hai yahan string be dal skte hain
# #     print(i) # isko print  karne k liye simple 

# """ ab isko karte hian sirf aur sirf string ke sath """
# for i in "Muhammed Kashif": # yeh hai for loop aur m kashi is a string in forloop
#     print(i)   # yeh be sahi hai aisa be kar skte hain
#     # output me m kashi hi ayegi no problem
number = input("enter a number : ")   # user input
total = 0   # total var hai
for i in number:
    total += int(i)   # int is liye input func sirf str me input lega
print(total)   # print karne k liye