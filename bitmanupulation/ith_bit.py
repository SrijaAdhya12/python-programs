# def ith_bit(n,i):
#     my_str = ""
#     while n > 0:
#         if n % 2 == 1:
#             my_str += "1"
#         else:
#             my_str += "0"
#         n = n//2
#     res = my_str[::-1]
#     if i < len(res):
#         if res[-(i+1)] == '1':
#             return True
#         else:
#             return False

# using bitwise opreator

def ith_bit(n,i):
    if (n>>i) & 1 == 0:
        return False
    else:
        return True



n = int(input())
i = int(input())
print(ith_bit(n,i))