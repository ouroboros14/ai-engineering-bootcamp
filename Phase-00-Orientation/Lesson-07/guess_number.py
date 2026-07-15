secret_number = 7

user_guess = int(input("Guess the secret number: "))

while user_guess:
    if user_guess == secret_number:
        print("Correct! You guessed the secret number.")
        break

    print("Wrong guess. Try again!")
    user_guess = int(input("Guess the secret number: "))