from collections import Counter

def word_frequency_counter(para):
    sentences = para.lower().split(".")
    words = [word for sentence in sentences for word in sentence.split()]
    my_dict = {}
    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

def word_frequency_counter(para):
    sentences = para.lower().split(".")
    words = [word for sentence in sentences for word in sentence.split()]
    my_dict = {word: words.count(word) for word in words}
    return my_dict
    
    
def word_frequency_counter(para):
    words = [word for sentence in para.lower().split(".") for word in sentence.split()]
    return Counter(words)

para = input("Enter a para: ")
print(word_frequency_counter(para))
