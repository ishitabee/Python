""" Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. 
Determine whether the Expression is balanced or not.
An expression is balanced if: 
Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order. """

def BraceBalance(expression):
    countOfOpenBraces = 0
    latestOpenBrace = ""

    for brace in expression:
        
        if brace in "({[":
            countOfOpenBraces += 1
            latestOpenBrace = brace

        
        elif brace in ")}]":
            countOfOpenBraces -= 1

            
            if countOfOpenBraces < 0:
                return False

           
            if latestOpenBrace == "(" and brace != ")":
                return False
            if latestOpenBrace == "{" and brace != "}":
                return False
            if latestOpenBrace == "[" and brace != "]":
                return False

            latestOpenBrace = ""
    
    if countOfOpenBraces > 0:
        return False

    return True

expression = input("Enter the expression: ")

if BraceBalance(expression):
    print("The braces are balanced.")
else:
    print("The braces are not balanced.")