"""Join and split method 
split method
 convert string to list
split method will convert strings in list"""

# split method
#user_info = "kashif 5".split()
#print(user_info)

"""for example merepass aik string hai userinfo aur isko list me karna chahta hun
aur isko wahan se todna chahta hun jahan se space hai
me use karunga split method ko"""

# user_info = "kashif 5".split() # style,tareeka
# for comma seprated banane k liye 
#user_info = "kashif,5".split(",")



"""Join method ===> convert list to string
for example humare pass hai list aur humne isko convert karna hai string mai"""

# Join method 
user_info = ['Hamza', "20"]
print(','.join(user_info))
# yeh hai method aur agar hum "20" ko int mai karunga to error ayega 