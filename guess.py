import random

DEBUG = False  # Set to True to enable debug mode


def ask_yes_no(question):

    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def ask_max_number():

    while True:
        try:
            max_number = int(
                input(
                    "Enter the maximum number for the guessing range (must be greater than 1): "
                )
            )
            if max_number > 1:
                return max_number
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a valid integer.")


def get_user_guess(max_number):

    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Please enter a valid integer.")


def play_game(max_number):

    score = 1
    random_number = random.randint(1, max_number)
    if DEBUG:
        print(f"[DEBUG] The random number is: {random_number}")

    print(
        f"I have selected a random number between 1 and {max_number}. Can you guess what it is?"
    )
    guess = get_user_guess(max_number)

    while guess != random_number:
        score += 1
        if guess < random_number:
            print("Your guess is too low. Try again!")
        elif guess > random_number:
            print("Your guess is too high. Try again!")
        guess = get_user_guess(max_number)

    print("Congratulations! You've guessed the correct number:", random_number)

    if score == 1:
        print("Amazing! You guessed it on your first try!")
    else:
        print(f"It took you {score} guesses.")


def ask_play_again():
    return ask_yes_no("Would you like to play again?")


def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        max_number = ask_max_number()
        play_game(max_number)
        if not ask_play_again():
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
