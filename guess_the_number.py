"""
The program will first randomly generate a number unknown to the user.
The user needs to guess what that number is.

If the user’s guess is wrong, the program should return some sort of
indication as to how wrong (e.g. The number is too high or too low).

If the user guesses correctly, a positive indication should appear.

You’ll need functions to check if the user input is an actual number,
to see the difference between the inputted number and the randomly
generated numbers, and to then compare the numbers.
"""


from random import randint

lucky_number = randint (1,100)

print ("Welcome to 'Guess the Number Game'.")
print ("I kept an integer between 1 and 100 in my mind.")
print ("Wanna guess what number I'm holding?")

while True:
    # Checking ValueError
    guess = input("\nCome on tell me your guess: ")
    
    try:
        guess = int(guess)
    except ValueError:
        print ("\nIt should be integer number!")
    else:
        break

    
while True:

    if guess == lucky_number:
        print ("\nCongratulations. Correct guess.")
        break
    
    elif guess != lucky_number:

        if guess > lucky_number:
            if guess == lucky_number+1:
                print ("\nToo close but high!")
            else:
                print ("\nToo high!")
        elif guess < lucky_number:
            if guess == lucky_number-1:
                print ("\nToo close but low!")
            else:
                print ("\nToo low!")

    while True:
        # Checking ValueError
        guess = input("Guess again: ")

        try:
            guess = int(guess)
        except ValueError:
            print ("\nIt should be integer number!")
        else:
            break


