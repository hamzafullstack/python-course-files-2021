# read and write
with open('0file1.txt', 'r') as rf:
    with open('0file2.txt', 'w') as wf:
        wf.write(rf.read())