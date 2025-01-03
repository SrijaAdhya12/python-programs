#Find the ASCII value of a character.'

def asc(char):
    return ord(char) #ord is used to find ASCII value of a character

my_char = input("Enter a character: ")
print(asc(my_char))
