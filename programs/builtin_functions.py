# bin() 
# bool()
# chr()
# complex()
# dict()
# dir() #class name is passed inside dir(class_name) returns methods of the class in a list
# float()
# help() #help(class_name) provides documentation for the class name pased in it and returns it in form of a string
# int()
# list()
# oct()
# pow()
# print()
# range()
# str()
# set()
# tuple()
# reversed()
# sorted()
# exec()
# eval()
# map()
# type()
# enumerate()


# print(dir(__builtins__)) ***

# count = 0
# for i in dir(__builtins__):
#     if i[0] == "_":
#         continue
#     if i[0].isupper():
#         continue
#     print(i)
#     count += 1
# print(count)


print(type(9))
print(type("strings"))
print(type((3,)))
print(type([8,0,12]))

a= (1,)
b= 1,