# super class,,

# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# aise be kar skte hain >>>...<<<

# def is_palindrom(word):
#     if word == word[::-1]:
#         return True

#     return False

def is_palindrom(word):
    return word == word[::-1]
print(is_palindrom("madam"))
print(is_palindrom("mard"))
#return w == w reverse str dekhega aur false and true dega # 