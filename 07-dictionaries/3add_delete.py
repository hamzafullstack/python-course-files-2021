# add and delete data
user_info = {
    'name' : 'Ameer hamza',
    'age' : 20,
    'fav_movies' : ["Batman", "The Dark knight", "The Dark Knight rise"],
    'fav_music' : ['Dil jo pako mehboob', 'Cartoon on & on', 'come on come on'],
}

# How to add data?

# user_info['fav_games'] = ['Tomb Raider', 'PUBG', 'Call of duty']
# print(user_info)

# Pop Method..............!!!

# popped_items = user_info.pop('fav_music')
# print(f"popped item is {popped_items}")
# print(user_info)

# TypeError ayegi agar pop() me kuch be pass na kare to
# at least koi key dena zaruri hai

# popped_item method.................!!!
#popitem method hum tab use karte hain jab humhe koi random key value delete krni

popitem = user_info.popitem()
print(user_info)

# popitem tuples return karega