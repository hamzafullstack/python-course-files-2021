winning_number = 32
guess = 1
number = int(input("Guess a number between 1 and 100 : "))
Game_over = False

while not Game_over:
    if number == winning_number:
        print(f"Victory...!!! You guessed this number in {guess} times")
        Game_over = True
    else:
        if number < winning_number:
            print("Too Low")
            guess += 1
            number = int(input("Guess Again : "))
        else:
            print("Too High")
            guess += 1
            number = int(input("Guess Again : "))
