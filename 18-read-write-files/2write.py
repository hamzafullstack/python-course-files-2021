# w, a, r+
with open('0sub.txt','r') as f: # w for overwrite (mode)
    data = f.read()
print(data)

# w mode kahan use karna chahiye
# w mode tab use karna chahiye jab humara file empty ho ya data delete karna na ho

# a mode for append
# a mode will not delete data from file this will append only

# r+ mode will not create any file 