# else and finaly clause in exception handling
while True:
    try:
        number = int(input("Enter a number: ")) # seven # 7 # ten #10
    except ValueError:
        print("invalid input...")
    except:
        print("Unexcepted Error...")
    else:
        print(f"user input = {number}")
        break
    finally:
        print("finally blocks") # yeh block hamesha chalega