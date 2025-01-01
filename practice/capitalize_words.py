#capitalise all word in a string



def capital_letters(line):
    words = line.split()
    new_word= ""
    for word in words:
        new_word += word.capitalize() + " "
    return new_word



def capital_letters(line):
    words = line.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)

sentence = input("Enter a sentence: ")
print(capital_letters(sentence))


my_list = ["Srija", "Pritam"]
my_str = " ".join(my_list)
print(my_str)

