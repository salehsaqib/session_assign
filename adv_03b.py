def main():            
    def ind_chk(ulist:list,ind:int)->bool:
        list_len:int = len(ulist)
        if (ind>=list_len) or (ind<(-list_len)):
            return False

    def acc_list(ulist:list,ind:int)->str:        
        if (ind_chk(ulist,ind)==False):
            return f"You are asking for out of range list element"
        return ulist[ind]
    
    def mod_list(ulist:list,ind:int,nval:str)->list:        
        if (ind_chk(ulist,ind)==False):
            return f"You are asking for out of range list element"
        ulist.insert(ind,nval)
        return ulist
    
    def slc_list(ulist:list,stind:int,enind:int)->list:        
        if (ind_chk(ulist,stind)==False) or (ind_chk(ulist,enind)==False):
            return f"You are asking for out of range list element"
        return ulist[stind:enind]
        
    
    fruit_list:list = ["apple", 5, "orange", 15.86, "pineapple", "mango"]
    while True:
        userChoice:str = str(input("Select an operation: A for Access - M for Modify - S for Slice - Q for Quit the Game: "))
        match userChoice:
            case 'A':
                userIndex:int = int(input("Enter position number to access from list: "))
                print(acc_list(fruit_list,userIndex))
            case 'M':
                userIndex:int = int(input("Enter position number to insert in the list: "))
                userItem:str = str(input("Enter item name to insert in the list: "))
                print(mod_list(fruit_list,userIndex,userItem))
            case 'S':
                stIndex:int = int(input("Enter Starting position of list: "))
                enIndex:int = int(input("Enter Ending position of list: "))                
                print(slc_list(fruit_list,stIndex,enIndex))
            case 'Q':
                break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
