def get_permutations(string, i=0):
    for j in range (i, len(string)):
        words = [c for c in string]
        words[i], words[j] = words[j], words[i]
        get_permutations(words, i+1)
    if i == len(string):
        print("".join(string))
        
str = input("Enter a string: ")
print(get_permutations(str))
        
        