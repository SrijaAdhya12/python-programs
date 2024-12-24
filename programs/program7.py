#CODE:To find prime number

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True

for i in range(1,101):
    result = is_prime(i)
    print(i , end=" ") if result else None    
