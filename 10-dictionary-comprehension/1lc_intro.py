# Dictionaries comprehension

square = {f"square of {num} is":num**2 for num in range(1,11) }
for k, v in square.items():
    print(f"{k} : {v}")

#word counter
string = "Hamza"
word_count = {char:string.count(char) for char in string}
print(word_count)