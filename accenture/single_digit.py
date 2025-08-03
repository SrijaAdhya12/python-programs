def single_digit(n):
    if n < 9:
        return n
    while n >= 10:
        if n % 2 != 0:
            n = n //2
        else:
            n = (n-2)//2
    return n


n = int(input())
print(single_digit(n))