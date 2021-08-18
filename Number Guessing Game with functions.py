import random

"""
The first function decide_range() decides on a range value. if the user picks 8, 
this value (stored in user_input) gets carried to the next function.
The second function guess_number() generates a random number between 1 and 8 (user_input). 
This function contains conditions to check if the user guesses correct,too low or too high.
A count is included in the second function to count the attempts it took for the user to 
guess correctly. Both the first and second function validate for a valid integer input 
using .isdigit(). The last function play_again() allows the user to decide if they want 
to play again or end the program
"""
def decide_range():
    flag = True
    while flag:

        user_input = input("Enter a value for range ")
        if user_input.isdigit():
            user_input = int(user_input)
            # print(f"Type is {type(user_input)}")
            if user_input < 2:
                print("Number must be 2 or greater to play this game")
                continue
            return user_input

            flag = False

        else:
            print("Not a valid integer")


def guess_number(x):
    random_number = random.randint(1, int(x))
    #print(f"Random number picked is {random_number}")
    attempts = 1
    flag = True
    while flag:

        user_input = input(f"Guess the random number between 1 and {x} ")
        if user_input.isdigit():
            user_input = int(user_input)

            if user_input == random_number:
                print(f"You guessed correct it took you {attempts} attempts")
                flag = False
            elif user_input > random_number:
                attempts += 1
                print("Try a lower number")
            elif user_input < random_number:
                attempts += 1
                print("Try a higher number")

        else:
            print("Not valid")


def play_again():
    flag = True
    while flag:
        print("")
        user_input = input("Would you like to play again yes/no").lower()
        if user_input == "yes":
            x = decide_range()
            guess_number(x)

        elif user_input == "no":
            print("Program ended")
            flag = False


x = decide_range()
guess_number(x)
play_again()
