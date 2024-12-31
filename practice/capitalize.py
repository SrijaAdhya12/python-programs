# CAPITALISE FIRST LETTER OF A SENTENCE

def capitalise(sen):
    return sen[0].upper() + sen[1:]


def capital(sen):
    return sen.capitalize()

sentence = input("enter a sentence: ")
print(capital(sentence))