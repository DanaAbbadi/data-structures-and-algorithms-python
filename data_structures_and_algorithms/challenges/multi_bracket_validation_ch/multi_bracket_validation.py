
def multi_bracket_validation(input):
    """
    Check if a string is balanced or not, the function takes a string as its only argument, and returns a boolean representing whether or not the brackets in the string are balanced.

    """

    open_tags = ["[","{","("] 
    closing_tags = ["]","}",")"] 
    check = [] 
    
    for i in input: 

        if i in open_tags: 
            check.append(open_tags.index(i)) 

        elif i in closing_tags: 
            if ((len(check) > 0) and (closing_tags.index(i) == check[-1])): 
                check.pop() 
            else: 
                return False

    if len(check) == 0: 
        return True
    else: 
        return False

        

if __name__ == "__main__":
    string = "{[]{()}}"
    print(string,"-", multi_bracket_validation(string)) 
    
    string = "[{}{})(]"
    print(string,"-", multi_bracket_validation(string)) 
    
    string = "((()pp))"
    print(string,"-",multi_bracket_validation(string)) 
   