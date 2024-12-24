"""
*

*
* *

*
* *
* * *

*
* *
*   *
* * * *

*
* *
*   *
*     *
* * * * *

"""
n=1
for i in range(n):
    if i==0 or i== n-1:
        print("* " * (i+1) , end="")
    else:
        for j in range(i+1):
            if j==0 or j==i:
                print("* " , end="")
            else:
                print("  " , end="")
    print()
