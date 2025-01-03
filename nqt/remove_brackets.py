# Remove brackets from an algebraic expression.

def remove_brackets(expn):
    return expn.replace("(" , "").replace(")" , "")
            
expression = input("Enter an algebric expression: ")
print(remove_brackets(expression))
