# Check if two strings are anagrams of each other.

# Two strings are anagrams if they contain same characters eith same frequency

def check_anagrams(str1 , str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if sorted(str1) == sorted(str2):
        return "The strings are anagram"
    return "The strings are not anagram"
    
    
strng1 = input("Enter a string: ")
strng2 = input("Enter another string: ")

print(check_anagrams(strng1, strng2))