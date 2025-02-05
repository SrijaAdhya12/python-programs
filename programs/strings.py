str_ = "Hello World"
str1 = """
Hello
World
"""
str2 = "Hello World"
print("Hello" * 3)


# Strings are immutable in nature
for i in "Hello World":
    print(i, end=" ")

print()

print(len(str_))  # whatever is passed in len() checks __len__ method (dunder method)
str(1234)
print(str_ + str1)

'"Pritam" is my husband'  # escape sequence


"'Pritam' is my husband"

'"Pritam" is my husband'  # escape sequence

"\n", "\t", "\\", '"', "'"

a, b = "He"
print(a)
print(b)

*_, lastchr = "HUIHUIHI"  # unpacking
print(lastchr)

*_, seclast, last = "srija"
print(seclast)
print(last)

a, *_, c = "srijapritam"
print(a)
print(c)

print("my" + "dumdu")
print("my"  "dumdu") # concatination can be done without + opreator too.

print("hi" 'shona')
str2= "hemlo" 'duddu' """my dear"""
print(str2)
template= "I am {} {}" #Template string
srija = template.format("Srija" , "Adhya")
pritam = template.format("Pritam" , "Kundu")
golu = template.format("Soumiti" , "Das")
rick = template.format("Rick" , "Sanchez")
morty = template.format("Morty" , "Smith")
print(srija , pritam, golu , rick, morty, sep="\n")

str2="my gublu is Pritam"
print(f"{str2.capitalize()=}")
print(f"{str2.count("i",-4)=}")
print(f"{str2.count("i",-9,-6)=}")
print(f"{str2.count("z")=}")
print(f"{str2.endswith("u")=}")
print(f"{str2.startswith("u")=}")
print(f"{str2.center(30)=}") #**
print(f"{str2.center(30,"*")=}") #**
print(f"{str2.center(30,"*")=}") #adds padding
print(f"{str2.find("i")=}") #finds the index of the passed string
print(f"{str2.find("z")=}") #gives -1 as output if character is not found
print(f"{"hello"<"hi"=}")
print(f"{"hello"<"hi"=}")
print(f"{template.format("Morty" , "Smith")=}") #finds the index of the passed string
print(f"{str2.index("i")=}") #finds the index of the passed string

#find retuens -1 when chr is not found but index raises an exception when chr is not present

print(f"{"1a".isalnum()=}") #finds the index of the passed string
print(f"{"*,1a".isalnum()=}") #finds the index of the passed string
print(f"{"VI".isalnum()=}") #finds the index of the passed string
print(f"{"*,1a".isalpha()=}") #finds the index of the passed string
print(f"{"aa".isalpha()=}") #finds the index of the passed string
print(f"{"cc66".isidentifier()=}") #finds the index of the passed string
print(f"{"AA".isupper()=}") #finds the index of the passed string
print(f"{"XX".isnumeric()=}") #finds the index of the passed string
print(f"{"XX".isdigit()=}") #finds the index of the passed string
#?isnumeric()= takes fraction, roman numerals, decimals isdigit()= takes only number

a = ("hello world", "pritam" , "srija" , "cutu", "duddu")
print(f"{ " ".join(a)=}") #joins a tupple
print(f"{ "*".join(a)=}") #joins with * in between
a = {"hello world", "pritam" , "srija" , "cutu", "duddu"}
print(f"{ " ".join(a)=}") #joins with * in between
print(f"{ "Pritam".replace("i","x")=}") #joins with * in between
print(f"{ "Pritam".swapcase()=}") #joins with * in between
print(f"{ " ".join(a).title()=}") #converts to title case
print(f"{ " Pritam".lstrip(" ").lstrip("P")=}") #joins with P in between
print(f"{ " Pritam ".strip(" ")=}") #removes space from sides
print(f"{ " Pritam ".rstrip(" ")=}") #removes space from right side
str1 =""
str2 =str()


*_, lastchr = "HUIHUIHI"  # unpacking
print(lastchr)

*_, seclast, last = "srija"
print(seclast)
print(last)

a, *_, c = "srijapritam"
print(a)
print(c)

a, *c, b = "H" "hi" "yy" "hi"
print(a,)
print(c)
print(b)
li= [c]
print(*li)
