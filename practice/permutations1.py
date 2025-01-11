from itertools import permutations

word = input("Enter a string: ")

perms = list(permutations(word))
for perm in perms:
    print("".join(perm))
    
    
r_perms = list(permutations(word, r=2))
for perm in r_perms:
    print("".join(perm))