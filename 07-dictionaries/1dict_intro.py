# introduction to dictionaries
""" Question """
# why we use Dictionaries??????
""" Answer """
# because of limitations of list, lists are not enough to represent reall data
""" Question """
# what are dictionaries??

""" Answer """
# unordered collection of data in key : value pair,,
# how to create dictionaries??
# we {} for dictionaries in python
user = {'name' : 'Ameerhamza', 'age' : 20}
# print(user)
# print(type(user))

# another method to create dictionaries with dict method
user1 = dict(name = 'Ameer Hamza', age = 20)
#print(user1)

""" Question """
# how to access data from dictionaries?????
""" Answer """
# NOTE :- There is no indexing, because of dictionaries are unordered collections
# of data
# NOTE :- in dictionaries we use keys to access data
# how to access??
#print(user(['name'])
# which type of data a dictionary can store ??
# anything
#int,str,float,dict,lists etc

# create a clean syntax dict... (seems Goooooooooooooood)
user_info = {
    'name' : 'Ameer hamza',
    'age' : 20,
    'fav_movies' : ["Batman", "The Dark knight", "The Dark Knight rise"],
    'fav_music' : ['Dil jo pako mehboob', 'Cartoon on & on', 'come on come on'],
}
#print(user_info['fav_movies']) # access key

# how to add data to empty dictionaries???
user_info2 = {}
user_info2['name'] = 'Muhammed Kashif'
print(user_info2)