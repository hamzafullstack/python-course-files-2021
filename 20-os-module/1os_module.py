import os
#os.getcwd() == pwd

# print(os.getcwd()) # get info location
# os.mkdir("Programmer") # make folder | dir
#  print(os.path.exists("programmer")) # check file exists or not true|false
# if os.path.exists('coder'):
#     print("Already exist")
# else:
#     os.mkdir('coder')

# create files using python
# open('file_one.txt', 'a').close()

# show list of files with python os module
# print(os.listdir())

# join....................
for item in os.listdir():
    path = os.path.join(os.getcwd(),item)
    print(path)