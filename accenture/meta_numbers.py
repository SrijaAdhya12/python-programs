def find_meta_numbers(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0 and i % 4 == 0 and i and i % 8 ==0 and i %10 != 0:
            count+=1
    return count


n = int(input())
print(find_meta_numbers(n))
