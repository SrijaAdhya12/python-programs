str1 = input("Enter a string")
for i,item in enumerate(str1):
    if i%2 != 0: print(item , end=" ")

for i,_ in enumerate(str1):
    ... #-> elipsis
    pass



print(list(input("enter string")[1::2]))


#enumerate takes an iterable to iterate and returns the pair of index and item.

for i in range(len(str1)):
    print(str1[i])

list1 = [1,2,3,4] 
for i,item in enumerate(list1):
    if i%2==0:
        print(item)   