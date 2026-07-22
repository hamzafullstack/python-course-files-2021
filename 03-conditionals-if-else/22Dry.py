# DRY don't Repeat yourself
import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("Guess a number between 1 and 100 : "))
Game_over = False

while not Game_over: #True for infinite Loop
    if number == winning_number:
        print(f"Victory...!!! You guessed this number in {guess} times")
        Game_over = True  # break for break
    else:
        if number < winning_number:
            print("Too Low")
        else:
            print("Too High")

        guess += 1
        number = int(input("Guess Again : "))
