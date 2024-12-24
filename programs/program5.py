def fact(n):
    # return n>=1 ? factn(n-1) : 1
    return n*fact(n-1) if n>=1 else 1

print(fact(5))