import random

print("Welcome to the Binary Search Game!")
print("I have selected a random number between 1 and 20.")
print("Try to guess the number in 3 attempts or less.")

secret_number = random.randint(1, 20)
attempts = 3

for attempt in range(1, attempts+1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess (1-20): "))
        if guess < 1 or guess > 20:
            print("Please enter a number between 1 and 20.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts.")    
        elif guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
    except ValueError:
            print("Invalid input. Please enter a valid integer between 1 and 20.")
else:
            print(f"Sorry, you've used all your attempts. The secret number was {secret_number}. Better luck next time!")