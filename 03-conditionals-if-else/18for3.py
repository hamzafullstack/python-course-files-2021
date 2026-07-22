# for loop example with user input
#
total = 0
n = input('enter the number : ') # for user input
for i in range(0, len(n)):
    total += int(n[i])
print(total)
