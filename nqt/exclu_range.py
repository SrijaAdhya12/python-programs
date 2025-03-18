#Given a range [m,n] both (inclusive) find the sum of integers between them


def inclusive_sum(m,n):
    sum = 0
    for i in range(m, n+1):
        sum += i
    return sum


num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
print(inclusive_sum(num1, num2))