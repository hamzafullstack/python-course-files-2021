# update method in dictionaries

user_info = {
    'name' : 'Ameer hamza',
    'age' : 20,
    'fav_movies' : ["Batman", "The Dark knight", "The Dark Knight rise"],
    'fav_music' : ['Dil jo pako mehboob', 'Cartoon on & on', 'come on come on'],
}

# update method........................!!!

more_info = {'state' : 'Sindh', 'Hobbies' : ['Hacking', 'coding', 'Reading Novel']}
user_info.update(more_info)
print(user_info)

"""agar hum same key dalengy to error nahi ayega na hi new name add hoga
simply update ho jayega key value
agar update() empty chorengy to kuch be change nahi hoga"""