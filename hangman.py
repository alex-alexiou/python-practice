import random
from guess import ask_yes_no

words = ["python", "hangman", "programming", "challenge", "developer"]


def choose_word():
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()


def guess_letter(guessed_letters):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
        else:
            return guess


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_remaining = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts_remaining > 0:
        guess = guess_letter(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts_remaining -= 1
            print(f"Wrong guess! Attempts remaining: {attempts_remaining}")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Sorry, you've run out of attempts. The word was:", word)


def main():
    while True:
        play_hangman()
        if not ask_yes_no("Do you want to play again?"):
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":

    main()
