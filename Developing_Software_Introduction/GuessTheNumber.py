import random

def guess(x):
    random_number = random.randint(1, x)
    num_guesses = 0
    AllGuesses = []
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        AllGuesses.append(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        num_guesses += 1

    print(f'Wow, congrats! You have guessed the number {random_number} correctly!')
    print(f'These are all the guesses you have tried: {AllGuesses}')

guess(25)
    
