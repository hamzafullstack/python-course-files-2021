#   Zip Function
user_id = ['user1', 'user2', 'user3']
names = ['hamza', 'Sattar', 'kashif']

# Zip function humhein object dega jis mai tuples hongy,,, jo iterator hoga
print(list(zip(user_id, names)))

#print(dict(zip(user_id, names))) # change in dict

# agar str  kam hain userid me 2 aur names me 3 to ziping 2 tak hogi

# change list into dictionary
example =  [('a', 1), ('b', 2)] #tuple in list
print(dict(example))

# koi be aisa list jis me tuples 2 value se le usko dict kar sakte hain