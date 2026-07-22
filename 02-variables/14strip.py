
""" Strip Method """

#strip method use kiya jata hai fazul spaces ko remove karne k liye code me se
# matlab ke string me se
""" lstrip """
""" lstrip and rstrip """

# name = "       Ham   za       "
# dots = "...................."
# print(name.lstrip()) #  Lstrip | for removing left side spaces
# print(name.rstrip()) #  rstrip | for removing right side spaces
# print(name.strip() + dots) #strip | for removing spaces from both sides

# # strip method bech wale spaces ko khatam nahi karega ham zaa
# # uske liye aik method hai

""" Replace method """

# print(name.replace(" " , "") + dots) #replace method
name = "    Ameer    Hamza   "
dots = "....................."
print(name.lstrip() + dots)    #lstrip method
print(name.rstrip() + dots)   #Rstrip method
print(name.strip() + dots) # strip method

#let se replace method for removing centre spaces
print(name.replace(" ", "") + dots) #replace method