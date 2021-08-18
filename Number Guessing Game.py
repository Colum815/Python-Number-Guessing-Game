entire_game_flag = True
while entire_game_flag:
    import random

    part_one = True
    while part_one:
        user_number_range = input("Enter a number for your range value ")
        if user_number_range.isdigit():
            user_number_range = int(user_number_range)
            if user_number_range < 2:
                print("Must be greater than or equal to 2")
                continue
            print(user_number_range)
            part_one = False
        else:
            print("Not a valid number try again")
    random_number = random.randint(1, user_number_range)
    print("Guess a number between 1 and ", user_number_range)

    part_two = True
    attempts = 0
    while part_two:
        attempts += 1
        user_guess = input("Guess the number ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Not a valid Number try again")
            continue

        if user_guess == random_number:
            print("You guessed correct it took you", attempts, "guesses")

            part_two = False
        else:
            if user_guess < random_number:
                print("Try a higher number")
            if user_guess > random_number:
                print("Try a lower number")
    replay_flag = True
    while replay_flag:
        user_play_again = input("Do you want to play again? yes/no").lower()

        if user_play_again == "yes":

            replay_flag = False

        elif user_play_again == "no":
            print("Program ended")
            replay_flag = False
            entire_game_flag = False
        else:
            print("Not a valid option")
            replay_flag = True
