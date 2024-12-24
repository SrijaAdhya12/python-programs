def sum1(num):
    s=0
    for i in range(num+1):s+=i 
    return s    



print(sum1(int(input("enter number"))))

num= int(input("enter a number"))
print((num*(num+1))//2)