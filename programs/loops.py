#Python only has : for each loop and while loop - entry condition loop

my_range = range(10)
for i in my_range:
    print(i , end=" ")

print()

for i in range(1,10):
    print(i , end=" ")

print()

for i in range(1,10,2):
    print(i , end=" ")

print()    
    
# for i in range(1,10,0): #!Error
#     print(i , end=" ")

print()

for i in range(1,10,99):
    print(i , end=" ")
 
print()

# infinite loop

while True:
    ...
    
while [1]:
    ...

# do while loop - exit condition loop

while 1:
    # statement 
    # condition
    break

age= 0

while 1:
    age +=1
    if age == 5:
        break




