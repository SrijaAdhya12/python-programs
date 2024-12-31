#CAPITALISE NTH LETTER OF A WORD

def capital_letter(w,i):
    try:
        if i < 0:
            raise IndexError("Index Value must be greater than zero")
        return w[:i] + w[i].upper() + w[i+1:]
    except IndexError:
        return "String index out of range"



word = input("Enter a word: ")
index = int(input("Enter the index to be capitalised: "))
print(capital_letter(word, index))