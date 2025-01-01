# list to string

my_list = input("Enter a list: ")
words = my_list.split()
for word in words:
    new_string = " ".join(words)
print(new_string)