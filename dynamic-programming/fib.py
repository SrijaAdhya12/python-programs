#WAF to calculate the n-1th fibonacci number

def fib(n):
    if n <=2:
         return 1
    return fib(n-1) + fib(n-2)

print(fib(6))

#using ternary operator
def fib(n):
     return 1 if n <= 2 else fib(n-1) + fib(n-2)
 

 #fibonacci has a time complexity of O(2^n) and space complexity of O(n)


# memorization

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(6))



#fibo using memorization
def fibo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

#time complexity of O(n) and space complexity of O(n)
