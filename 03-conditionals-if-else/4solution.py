#winning game
winning_number = 23
user_input = input("Guess a number b/w 1 and 100 : ")
user_input = int(user_input)
if user_input == winning_number: #for checking equality we use ==
    print("YOU WIN..!!!!")
else: #nested if else
    if user_input < winning_number:
        print("Too Low")
    else:
        print("Too High")