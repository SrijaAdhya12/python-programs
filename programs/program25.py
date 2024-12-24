"""
0 1 2 3
* * * * 0
* * * * 1

* * * * * * * *
* * * * * * * *
* * * * * * * *
* * * * * * * *

"""
n= int(input("enter n"))  
for i in range(n):
    for j in range(2*n):
        print("* " ,end="")
    print()    

n = int(input("enter n"))
for i in range(n):
    print("* " * 2*n)