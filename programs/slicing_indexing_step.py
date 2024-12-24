# String indexing:
my_str = "Pritam loves Srija"
# 1) positive
print(my_str[0])  # first character
print(my_str[1])  # any character
print(my_str[len(my_str) // 2 - 1])  # middle character
print(my_str[len(my_str) - 1])  # last character

# 2) negative
print(my_str[-1])  # last character
print(my_str[-2])  # secondlast character
print(my_str[-len(my_str)])  # first character

# string slicing
my_str = "Pritam loves Srija"
# 1) positive
print(my_str[:6])  # it is equivalent to my_str[0:6] , first 5 characters of a string
print(my_str[7:])  # it is equivalent to my_str[7:length-1] , skips first 6 characters
print(my_str[13:])  # it is equivalent to my_str[13:length-1]
print(my_str[7:12])  # it is equivalent to my_str[7:12]
print(my_str[7:99])  # it is equivalent to my_str[7:length-1]

# 2) negative
print(my_str[-5:])  # it is equivalent to my_str[-5:0]
print(my_str[:])  # it is equivalent to my_str[whole string]
print(my_str[-11:-6])  # it is equivalent to my_str[-11:-6]
print(my_str[:-5])  # skips last 5 characters
print(my_str[-99:])  # whole string

# 3) mixed
print(my_str[6:-5])  # skips first and last 5 chr
p = my_str[:6]  # pritam
s = my_str[-5:]  # srija
print(p)
print(s)

# step slicing
my_str = "Pritam loves Srija"
print(my_str[::])  #it is equivalent to my_str[::1], 1 is the default value of step (which means it skips 0 chr as default)
print(my_str[::2])  # skips 1 chr 
print(my_str[1::2])  # skips first and last 5 chr
print(my_str[::4])  # skips first and last 5 chr
# print(my_str[::0])  #! raises ValueError if 0 is provided in sliced step
print(my_str[::-1])  #*** reverses a string


print(my_str[-5:])  # it is equivalent to my_str[-5:0]
print(my_str[:-5])  # skips last 5 characters
print(my_str[1::2])  # skips first and last 5 chr
print(my_str[::4])  # skips first and last 5 chr
print(my_str[::2])  # skips 1 chr
