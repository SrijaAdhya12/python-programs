from itertools import combinations, combinations_with_replacement

letters= "ABCD"

# doesn't allow repetations
combs = list(combinations(letters, 2))
for comb in combs:
    print("".join(comb))
    
# does allows repetation
combs = list(combinations_with_replacement(letters,2))
for comb in combs:
    print("".join(comb))
    
