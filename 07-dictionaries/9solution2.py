user = {} #empty dictionary
# geting input from users
name =  input("what is your name : ")
age = int(input("what is your age : "))
fav_movies = input("your favourite Movies seprated by comma : ").split(',')
fav_songs = input("your favourite songs by seprated comma : ").split(',')
# appending/adding data in empty dictionary
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
# looping on dictionary
for key, value in user.items():
    print(f'{key} : {value}')