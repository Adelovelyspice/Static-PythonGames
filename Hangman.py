import random

def choose_word():
    # List of words for the game
    words = ["python", "hangman", "computer", "programming", "keyboard", "mouse", "developer", "game", "code", "algorithm"]

    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Enter a letter: ").lower()

        # Check if the input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print("Correct guess!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts_left -= 1

    if attempts_left == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
