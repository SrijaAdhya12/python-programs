#capitalise all word in a string

def capital_letters(line):
    words = line.split()
    new_word= ""
    for word in words:
        new_word += word.capitalize() + " "
    return new_word


sentence = input("Enter a sentence: ")
print(capital_letters(sentence))