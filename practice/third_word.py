#THIRD WORD OF THE STRING

def third_word(line):
    words = line.split()
    return words[2]

sentence = input("Enter a sentence: ")
print(f"The third word is: {third_word(sentence)}")