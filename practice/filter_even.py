my_list = [2,4,1,3,7]
print([num for num in my_list if not num % 2])
print(sum(1 for num in my_list if not num % 2))