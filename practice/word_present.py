# FIND A WORD IN A SENTENCE

def find_word(sen,req):
    words = sen.split()
    if req in words:
        return f"{req} the word is present and its occurs {words.count(req)}"
    return "Not Present"


sentence = input("Enter a sentence: ")
req= input("Enter the word required: ")
print(find_word(sentence, req))