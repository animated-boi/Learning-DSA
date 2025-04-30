import random

number = random.randint(1, 100)
guess = -1
no_of_guesses = 0

while ( guess != number):
    guess = int(input("Enter you guess (1 - 100) : "))
    
    if (guess < number):
        print(" Guess a higher number!")
    elif (guess > number):
        print("Guess a lower number!")

    no_of_guesses += 1

print(f"You guessed the number {number} right in {no_of_guesses} guesses!" )
