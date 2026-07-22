# word counter
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('Hamza'))

""" dictionary ka koi sahe order nahi hota yeh unordered hota hai """