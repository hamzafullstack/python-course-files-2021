number = input("Enter a number : ")   #user input
# "12345" length = 4 , last index = 3
# int(number [i])
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)