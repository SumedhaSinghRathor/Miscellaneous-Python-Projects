import random
n = random.randrange(1,10)
guess = int(input("Enter any number between 1 to 10: "))

while (n != guess):
    if guess < n:
        print('Go Higher')
        guess = int(input("Enter a number again: "))
    elif guess > n:
        print('Go Lower')
        guess = int(input("Enter a number again: "))
    else:
        break

print('You guessed it right!!')
        
