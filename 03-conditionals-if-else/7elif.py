# # if elif else statement in python
# #agar humhe multiple conditions test karne hain to iske liye elif is best option
# age = input("please enter your age :")
# age = int(age)
# if 0<age<=3:
#     print("Ticket Price : Free..!")
# elif 3<age<=10:
#     print("Ticket Price : 150")
# elif 11<age<=60:
#     print("Ticket Price : 250")
# else:
#     print("Ticket Price : 200")

age = input("Please enter your age: ")
age = int(age)
if 0<age<=3:
    print("Ticket is free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 11<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")