import random
secret_number = random.randint(1, 100)
guess_count = 0

print("Welcome to the guessing game!")
print("You need to guess a number from 1 to 100.")

while True:
    guess = int(input("What is your guess? "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations!")
        print("You guessed the secret number in", guess_count, "guesses!")
        break
    elif guess < secret_number:
        print("Guess is too low.")
    else:
        print("Guess is too high.")

'''Example output:
Welcome to the guessing game!
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Guess is too high.
What is your guess? 10
Guess is too high.
What is your guess? 5
Guess is too high.
What is your guess? 1
Guess is too low.
What is your guess? 2
Guess is too low.
What is your guess? 3
Congratulations!
You guessed the secret number in 7 guesses!
'''

print("end of program.")