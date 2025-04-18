def gcd(A,B):
    while B != 0:
        A,B = B, A%B
    return A

def lcm(A,B):
    lcm = A*B/gcd(A,B)
    return lcm



A = int(input("Enter a number: ")) 
B = int(input("Enter another number: ")) 
print(int(lcm(A,B)))