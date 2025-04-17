def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_series(n):
    count = 0
    num = 2
    if n == 1:
        return 2
    while True:
        if is_prime(num):
            count+=1
            if count == n:
                return num
        num += 1


num = int(input("Enter m: "))
num1 = int(input("Enter n: "))
arr = []
for i in range(num , num+num1+1):
    new_num =  prime_series(i)
    arr.append(new_num)
    sumation = sum(arr)
print(sumation)

    

