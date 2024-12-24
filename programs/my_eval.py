# str1 = """
# print("Hello world")
# """

# a= exec(str1)
# print(a)

# a= eval(str1)
# print(a)

# b= eval(s)


str1= str([1,2,3,4])
a = exec(str1)  #exec= execution, returns nothing
print(a)


a = eval(str1) #eval= evaluation, returns execution
print(a)
print(type(a))