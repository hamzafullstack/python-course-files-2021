
# inKeyword and iterations in dictionaries..

user_info = {
    'name' : 'Ameer hamza',
    'age' : 20,
    'fav_movies' : ["Batman", "The Dark knight", "The Dark Knight rise"],
    'fav_music' : ['Dil jo pako mehboob', 'Cartoon on & on', 'come on come on'],
}

"""check if key exist in dictionaries # ----> keys"""

# if 'name' in user_info:
#     print("Present")
# else:
#     print("Not Present")

"""check if values exist in dictionary ----> values method in dictionaries"""

# if 'Ameer hamza' in user_info.values():
#     print("Present")
# else:
#     print("Not Present")

"""Loops in dictionaries.... # ----> looping in dictionaries"""

#for i in user_info:
    #print(i)

"""is se sirf keys print hongi value pairs nahi
agar humhe sari values chahiye to hum use karengy"""

# for i in user_info.values():
#     print(i)
"""is se sirf values LOOOOP hogay"""

"""value method...............................!"""

# user_info_values = user_info.values()
# print(user_info_values)
# # is se sirf values print hongi list style me

"""keys method................................!"""

# user_info_keys = user_info.keys()
# print(user_info_keys)

"""loop values in dictionaries an other method"""

# for i in user_info:
#     print(user_info[i])

"""   items method         important, most usefull method"""
# user_items = user_info.items()
# print(user_items)
# tuples ki tarha return kar raha

for key, value in user_info.items():
    print(f"key is {key} value is {value}")