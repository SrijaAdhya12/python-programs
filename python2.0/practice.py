#lambda function


print((lambda x: x * 2)(2))

nums = [1,2,4,8,16,12]
my_list = [n for n in nums if not n % 2]
print(my_list)

my_list = [n ** 2 for n in nums]
print(my_list)

my_list = list(map(lambda n: n + 1, nums))
print(my_list)

age = 25

health = "Poor" if age > 60 else "Good"
print(health)

array = {1,2,3,4,5,6,7,8}
a ,b, *all, sl, l = array
print(a)
print(b)
print(all)
print(sl)
print(l)



nested_list = [1,2,[2,3]]
a,b,(c,d) = nested_list