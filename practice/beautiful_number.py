def check_beautifulnumber(num):
    for i in range(num):
        xor_res = i ^ num

    return xor_res == num

def cal_beautifulnumber(lst):
    count = 0
    for num in lst:
        if check_beautifulnumber(num):
            count += 1
    return count


arr = list(map(int, input().split(" ")))
print(cal_beautifulnumber(arr))

    
