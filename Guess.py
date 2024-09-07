import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user correctly guesses the number
while True:
  # Prompt the user to input their guess
  guess = int(input("Enter your guess: "))

  # Increment the number of attempts
  attempts += 1

  # Compare the guess to the secret number
  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")
  else:
    print(f" Congratulations! You guessed the number in {attempts} attempts.")
    break
