def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num %i == 0:
            return False
    return True

def m_prime(m):
    count = 0
    num = 2
    if m == 1:
        return 2
    while True:
        if is_prime(num):
            count+=1
            if count == m:
                return num
        num += 1

def summation(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num 



m = int(input("Enter num 1 (m):"))
res = m_prime(m)
res1 = summation(res)
print(res*res1)