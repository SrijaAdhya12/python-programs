def find_land(n):
    land = []
    sum = 0
    if n ==1:
        return 1
    for i in range(1,n+1):
        land.append(i)

    for j in range(1,len(land)):
        sum += land[j-1] ^ land[j]
    return sum



n = int(input()) 
print(find_land(n))