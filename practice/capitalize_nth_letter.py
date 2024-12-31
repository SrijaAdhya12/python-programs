#CAPITALISE NTH LETTER OF A WORD

def capital_letter(sen,index):
    words = sen.split()
    new_word = ""
    for word in words:
        new_word = word[:index] + word[index].upper() + word[index+1:]
    return new_word



word = input("Enter a word: ")
index = int(input("Enter the index to be capitalised: "))
print(capital_letter(word, index))