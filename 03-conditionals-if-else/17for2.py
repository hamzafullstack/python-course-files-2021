# #sum from 1 to 10
# # using for Loop   ----> range function
# # 1 + 2 = 3.....................10
# total = 0
# for i in range(1,11): # i variable hai iski jaga hum kuch be likh sakte etc
#     total += i # i is a variable
# print(total)

num = int(input("Enter the natural number : "))
total = 0
for i in range(1,num+1):
    total += 1
print(total)