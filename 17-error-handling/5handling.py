while True:
    try:
        age = int(input("Enter your age: ")) # seven # 7 # ten #10
        break
    except ValueError:
        print("invalid input...")
    except:
        print("Unexcepted Error...")
if age < 18:
    print("you can play game")
else:
    print("sorry you can't ")