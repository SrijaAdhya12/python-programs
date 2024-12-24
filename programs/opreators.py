# 1) Arithmetic opreators
a,b=1,2
print(f"{a+b=}")
print(f"{a/b=}")
print(f"{a%b=}")
print(f"{a*b=}")
print(f"{a-b=}")
print(f"{a**b=}")
print(f"{a//b=}")

# 2) logical opreators
a,b=True,False
print(f"{a or b=}")
print(f"{not a=}")
print(f"{a and b=}")
print(f"{not b=}")

# 3) assignment opreator
c=4
a+=3
b-=5 # b=b-5
c*=5
c/=5
c%=5
c**=5
c//=5
a&=b
a|=b
a^=b
a<<=b
a>>=b


# 4) identity opreator
print(f"{a is a=}")
print(f"{a is b=}")
print(f"{a is not b=}")
print(f"{1 == 1.0=}")
print(f"{1 is 1=}")

# is opreator checks value and memory address
# == checks only value

# 5) Membership opreators
my_list= [1,3,2,34]
print(f"{1 in my_list = }")
print(f"{"1" in my_list = }")
print(f"{my_list not in my_list = }")
my_list.append(my_list)
print(f"{my_list in my_list = }")


# 6) comparison opreators
a,b=5,8
print(f"{a == b =}") 
print(f"{a <= b =}")
print(f"{a >= b =}")
print(f"{a != b =}")
print(f"{a < b =}")
print(f"{a > b =}")

# 7) bitwise opreator
a,b= 0b110,0b100
print(f"{a&b= : b}")
print(f"{a|b= :b}")
print(f"{a^b= :b}")
print(f"{~a= :b}")
print(f"{a>>1= :b}")
print(f"{b<<1= :b}")
