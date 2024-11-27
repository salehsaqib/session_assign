import random

def main():        
    compGuess = random.randrange(0,99)
    userGuess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    while True:
        if (userGuess > compGuess):
            userGuess = int(input(f"Your guess {userGuess} is too high Enter a lower number: "))
        if (userGuess < compGuess):
            userGuess = int(input(f"Your guess {userGuess} is too low Enter a higher number: "))
        if (userGuess == compGuess):
            print(f" Congrats! {userGuess} is correct.")    
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()