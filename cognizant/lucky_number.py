
def find_luckynumber(my_list):
    arr = []
    sumation = 0
    product = 1
    for i,v in enumerate(my_list):
        asc_val = ord(v)
        product = asc_val*(i+1)
        if asc_val % 2 != 0 or i+1 %2 != 0:
            sumation += product
    return sumation



my_list = list(map(str,input().split()))
print(find_luckynumber(my_list))