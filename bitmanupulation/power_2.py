#brute force is if there is 1 set bit then it is a power of 2


def power_of_2(n):
    if n & (n-1) == 0:
        return True
    return False



n = int(input())
print(power_of_2(n))
