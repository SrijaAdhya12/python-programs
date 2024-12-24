# import this
# import __hello__

#construct a new sentence with spaces between the words for a user input in which the words are of length 6 

sent = input("Enter a sentence")
words= sent.split()
my_list= []
for word in words:
    if len(word) ==6:
        my_list.append(word)
print(" ❤️ ".join(my_list))        