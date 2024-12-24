""" 
*

* * 
* *

* * * 
*   *  3=2
* * *  n-1

* * * *  4=3
*     *
*     * n-1
* * * *

"""

n=4
for i in range(n):
    if i ==0 or i == n-1:
        print("* " * n)
    else:
        print("* " + "  "*(n-2) +"*")    
