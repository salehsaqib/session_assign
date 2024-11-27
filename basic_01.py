def main():
    PROMPT = "Welcome to my Funny Bot! Enter the Word Joke or JOKE : "
    JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
    SORRY = "I only programmed to tell jokes"
    userResponse = str(input(PROMPT))
    userResponse = userResponse.strip()
    if (userResponse=='Joke' or userResponse=='JOKE'):
        print(JOKE)
    else:
        print(SORRY)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()