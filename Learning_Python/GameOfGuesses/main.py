import random

number = random.randint(1, 100)
guess = -1
no_of_guesses = 0

while ( guess != number):
    no_of_guesses += 1
    guess = int(input("Enter you guess (1 - 100) : "))
    
    if (guess < number):
        print(" Guess a higher number!")
    else:
        print("Guess a lower number!")

print(f"You guessed it right in {no_of_guesses} guesses!" )
