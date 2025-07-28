def iterate(n):
    i = 0
    while i < n:
        i+=1
        yield i



x  = iterate(5)

try:
    while True:
        print(next(x))
except StopIteration:
    ...

