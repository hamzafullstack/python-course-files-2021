with open('lovestory.txt', 'r', encoding='utf-8') as lover:
    print(lover.encoding)
    data = lover.read()
    print(data)