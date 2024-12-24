my_list = []
my_list = list()
my_list.append(1)
my_list.append(15)
my_list.append(29)
my_list.append("13")
my_list.append((2,))
my_list.append({"hello" , "world"})
my_list.append({0:22})
print(my_list)

food= ["pasta" , "biriyani", "chicken" , "lasagna"]
food1= ["pizza" , "burger", "icecream" , "pritam"]
food2= ["pizza" , "burger", "icecream" , "pritam"]
food3= food2
print(f"{food+food1 = }")
print(f"{food == food1 = }")
print(f"{food1 == food2 = }")
print(f"{food1 is food2 = }")
print(f"{food2 is food3 = }")
food2.append("firni")
food2.insert(0, "coke")
print(f"{food2 = }")
print(f"{food2 = }")
print("food" if food>food1 else "food1")

num_list = [12,8,4,2,0,-1]
fst,sec, *_, last = num_list
print(fst)
print(sec)
print(last)
print(num_list[4])
print(num_list[1:5])
print(num_list[1::2])
print(num_list[1:-1])
print(len(num_list))
print((num_list)*3)
print(list(reversed(num_list)))
print(num_list[::-1])
print(sorted(num_list))
print(sorted(num_list, reverse=True))
num_list *= 3
print(num_list)
print(num_list.pop()) 
print(num_list.pop(1)) #removes 1st index
print(num_list)
num_list.clear()
print(num_list)
num_list.copy()


list1 = []

for i in range(10):
    list1.append(i+1)
print(list1)


list1= list(range(2,21,2))
print(list1) 


list2= list(range(1,11))
list3=[]
for i in list2:
    list3.append(i**2)
print(list3)        
list3.clear()
print(list3)


# list comprehension

print([i**2 for i in list2])


print([i**2 for i in list2 if i%2==0])
print([i**2 for i in list2 if i%2!=0])
print([i**2 if i%2==0 else i**2+1 for i in list2])
print(len([(i,j) for i in range(1,11) for j in range(1,11)]))

my_list=[1,7.2,5]
print(*my_list , sep=",")
print(*my_list , sep=" ")
print(*my_list , sep="\n")

my_list, *var =[1]  #unpacking a single element of a list
print(my_list)
print(var)

nested_list = [[1,2] , 3 , 4 ,5]
(a,b), *unused = nested_list
print(a,b)
[a,b], *unused = nested_list
print(a,b)
# {a,b}, *unused = nested_list  # {} can't do unpacking
# print(a,b)
print(unused)
print(*nested_list)
print("hello world")
print()
print("hello world")

# In C/C++ the printf() and scanf() has a return type int. Printf() returns the outputs.spaces and tabs & scanf() returns the input no. spaces and tabs.

list1 = [1,6,3,2]
print(id(list1))