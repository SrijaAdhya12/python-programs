# list to string

my_list = input("Enter a word: ")
words = my_list.split()
new_string = ""
for word in words:
    new_string += word + " "
print(new_string)