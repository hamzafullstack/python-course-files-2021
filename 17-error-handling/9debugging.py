import pdb # Python debugger # module
# module=>python file contains with usefull classes & functions wrote by devlopers

# definition of Debugging:-
"""
Debugging is a process of finding and resolving defects or problems within a
computer program,, that prevent a correct operations of computer program or system
"""
pdb.set_trace()
name = input("enter your name : ")
age = int(input("enter your age : "))
print(f"hello your name is {name} and your age is {age}")
age2 = age + 5
print(f"hello {name} you will be {age2} in next five years ")

# pdb cmds
# l for shows list
# n for run // execute
# c for continue code
# q for quite