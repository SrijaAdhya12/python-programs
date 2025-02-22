def longest_subsequence(text1 , text2):
    set1 = set(text1)
    set2 = set(text2)
    
    common = set1 & set2
    print(common)
    return len(common)

text1 = input("Enter text 1: ")
text2 = input("Enter text 2: ")
print(longest_subsequence(text1,text2))
