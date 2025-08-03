# number of pieces n straight lines can create


# 0 - 1
# 1 - 2
# 2 - 4
# 3 - 7
# n * (n-1) //2 + 1

def find_cakepieces(n):
    return n*(n-1)//2 +1

n = int(input())
print(find_cakepieces(n))
