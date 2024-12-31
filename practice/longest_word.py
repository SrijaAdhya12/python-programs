#LONGEST WORD IN A STRING

def find_longest_word(sen):
    words = sen.split()
    longest_word=""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


sen = input("Enter a sentence: ")
print(find_longest_word(sen))