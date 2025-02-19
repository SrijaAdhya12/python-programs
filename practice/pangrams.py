from string import ascii_lowercase as alphabets
from string import ascii_uppercase as upper_alphabets
import string 
from string import digits as decimal_digits
from string import punctuation as pun
def find_panagram(my_str):
    lower_sentence = my_str.lower()
    for char in alphabets:
        if char not in lower_sentence:
            return "not pangram"
    return "pangram"
 
    
my_str = input("Enter a string: ")
print(find_panagram(my_str))
# print(alphabets)
# print(upper_alphabets)
# print(decimal_digits)
# print(pun)
# help(string)