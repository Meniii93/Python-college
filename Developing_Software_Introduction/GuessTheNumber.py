import random
  
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    AllGuesses = []
    while guess != random_number:
        
        
        AllGuesses.append(guess)
        if guess < random_number:
            print('Sorry, guess again, Too low.')
        elif guess > random_number:
            print('Sorry, guess again, Too high.')
            
    print(f'Wow, congrats, you have guessed the number {random_number} correctly!')
    print(f'These are all the guesses you have tried:  {AllGuesses}')
            
guess(25)
    