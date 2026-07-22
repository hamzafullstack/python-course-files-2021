with open('0salary.txt', 'r') as rf:
    with open('output.txt', 'a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',') # name and salary | variables
            wf.write(f"{name}'s salary is {salary}") # F stringformating 3.6