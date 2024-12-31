"""
- CAPITALISE FIRST LETTER OF A SENTENCE
- CAPITALISE NTH LETTER OF A SENTENCE
- 3RD WORD OF STRING
- CAPITALISE ALL LETTERS IN SENTENCE
- CONVERT STRING TO LIST
- WORDS TO STRING
- SEARCH A SPECIFIC WORD IN A STRING AND ITS NUMBER OF OCCURANCE
- LONGEST WORD IN A STRING

"""

# CAPITALISE FIRST LETTER OF A SENTENCE

"""def capitalise(sen):
    return sen[0].upper() + sen[1:]

sen = input("enter a sentence")
print(capitalise(sen))"""


"""def capital(sen):
    return sen.capitalize()

sen = input("enter a sentence")
print(capital(sen))"""


#THIRD WORD OF THE STRING

"""def third_word(sen):
    words = sen.split()
    return words[2]


sen = input("enter a sentence")
print(third_word(sen))"""

#capitalise all the letters in a string

"""def capital_letters(sen):
    return sen.upper()

sen = input("Enter a sentence")
print(capital_letters(sen))"""

# CONVERT STRING TO LIST

"""def convert_to_list(sen):
    print(list(sen))


sen = input("Enter a sentence")
print(convert_to_list(sen))"""

# FIND A WORD IN A SENTENCE

def find_word(sen,req):
    words = sen.split()
    if req in words:
        return f"{req} the word is present and its occurs {words.count(req)}"
    return "Not Present"


sen = input("Enter a sentence")
req= input("Enter the word required ")
print(find_word(sen, req))