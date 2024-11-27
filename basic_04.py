import random

def main():        
    str_rnd = ""
    for i in range(10): 
        str_rnd = str_rnd + str(random.randrange(1,100)) + " "
    print (str_rnd)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()