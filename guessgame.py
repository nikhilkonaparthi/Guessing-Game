import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 5
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Correct! You win!")
                break
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print("You have no attempts left. You lose.")
            print(f"The correct number was {number_to_guess}.")

# Run the game
guess_number()
