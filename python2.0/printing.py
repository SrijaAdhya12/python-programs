#list of numbers
numbers = [1,2]

print(*numbers) #normally print all the numbers

print(*numbers, sep= "-") #changes seperator element

print(*numbers, end=" <-- end of numbers") #changes end of line

print("\n\n Print with both different seperator and end", sep = "->" , end="->")
