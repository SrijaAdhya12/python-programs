"""
n=1 
*
n=2
* *
* *
n=3
* * *
* * *
* * *
"""

n = int(input("Enter n"))
for i in range(n):
    for j in range(n):
        print("* " ,end=" ")
    print()
    

