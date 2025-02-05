
# my_list = [*map(int,input().split())] 
# my_list1 = [*my_list,*my_list]
# my_set = {*my_list,*my_list}

# for i in my_set:
#     print(i, "set")

# for i in my_list1:
#     print(i)


# my_list = [1]
# print(my_list, type(my_list))


# my_dict = {"a": 1}

lst1 = [1,2,3,4]
lst2=lst1
lst2= [*lst1]
lst2[3] = 5
print(lst1) #[1,2,3,5]


my_tuple = (1,)
print(my_tuple, type(my_tuple))

my_str = "s r i j a "
my_tuple = tuple(my_str)
print(my_tuple)


