# Sum of 10 multiples of a given number

def multiples(num):
    total = 0
    for i in range(1,num+1):
        total += num*i
    return total


num = int(input())
print(multiples(num))
