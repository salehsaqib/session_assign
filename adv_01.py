import random
def main():            
    print("----------------Welcome to the High-Low Game!-------------------")    
    userPoints=0
    for i in range(1,6,1):
        compNo = int(random.randrange(1,100))
        userNo = int(random.randrange(1,100))
        print(f"\n\n----------------------Round {i}--------------------------") 
        print(f"Your number is {userNo} \nDo you think your number is higher(H) or lower(L) than the computer's?:")    
        userChoice = str(input("Enter H or L : "))
        if (userChoice=='H' or userChoice=='h'):
            if(userNo > compNo):
                print(f"You were right! The computer's number was {compNo}")
                userPoints+=1    
            else:
                print(f"Aww, that's incorrect. The computer's number was {userNo}")
        if (userChoice=='L' or userChoice=='l'):
            if(userNo < compNo):
                print(f"You were right! The computer's number was {compNo}")
                userPoints+=1    
            else:
                print(f"Aww, that's incorrect. The computer's number was {userNo}")
    match userPoints:
        case 5:
            print(f"\nWow! You played perfectly!\nYour Total Points are {userPoints}")
        case 4:
            print(f"\nYour performance is Excellent\nYour Total Points are {userPoints}")
        case 3:
            print(f"\nGood job, you played really well!\nYour Total Points are {userPoints}")
        case 2:
            print(f"\nBelow Average !\nYour Total Points are {userPoints}")
        case 1:
            print(f"\nBetter luck next time!\nYour Total Points are {userPoints}")
        
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()