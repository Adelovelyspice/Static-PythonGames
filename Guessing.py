import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        guess = input("Enter your guess (or 'quit' to end the game): ")
        
        # Check if the player wants to quit
        if guess.lower() == 'quit':
            print("Thanks for playing! The number was", secret_number)
            break
        
        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You've guessed the number in", attempts, "attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    guess_number()

