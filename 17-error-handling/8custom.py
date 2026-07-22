class ShortNameError(ValueError):
    pass

def validate(Name):
    if len(Name) < 8:
        raise ShortNameError('Name is to short ')

user_name = input("Enter Your Name : ")
validate(user_name)
print(f"Hello Dear {user_name}")