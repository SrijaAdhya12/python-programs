#In shell the _ returns the last evaluated expression
#In python the underscore is used as a placeholder for a variable that is not used

data = [(1, 'one'), (2, 'two'), (3 , 'three')]
for _, word in data:
    print(word)
