# read files

# open function

file_one = open('0file.txt') # r for read file
print(f"cursor position {file_one.tell()}") # tell check our cursor,,
print(file_one.read()) # read file in string
print(f"cursor position {file_one.tell()}")
print(file_one.read())
file_one.close() # for closing file


# seek method | file_one.seek(0) # set pos for cursor

# readline method | file_one.readline()) # read files line by line
# for remove extra spaces in lines file_one.readline(), end='')

# readlines method | check how much lines are in file

# datadiscriptors ==> name , closed (they are not functions) print(file_one.name)