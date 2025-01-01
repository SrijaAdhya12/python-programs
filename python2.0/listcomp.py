people: list[str] = ['Srija', 'Pritam' , 'Mario', 'Stephanny']

long_names: list[str] = [p for p in  people if len(p) > 5] 
print(f"Long Names: {long_names}")

#list comprehension

nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [n*n for n in nums ]
print(my_list)

my_evenlist = [n for n in nums if n%2==0]
print(my_evenlist)

#map + lamda

my_list = map(lambda n : n*n, nums) 
print(list(my_list))

#lambda + filter

my_evenlist = filter(lambda n: n%2==0, nums)
print(list(my_evenlist))


#dictionary comprehension
names = ['Srija', 'Pritam', 'Mario', 'Stephanny']
marks = [80, 90, 70, 60]

my_dict= {name: mark for name, mark in zip(names, marks)}
print(my_dict)

#set comprehension

nums = {1,2,3,4}
my_set = {n*n for n in nums}
print(my_set)

# tuple comprehension

nums = (1,2,3,4)
my_tuple = tuple(n*n for n in nums)
print(my_tuple)


#ternary + list comprehension

numbers = range(1,11)
odd_even_list = [n if n%2 == 0 else "odd" for n in numbers]
print(odd_even_list)


num = range(1,11)
my_list = ["divisible by 5" if n%5 == 0 else "not divisible" for n in num]
print(my_list)


#nested list comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_list = [n for row in matrix for n in row]
print(my_list)

for i in range(6,8):
    for j in range(4,7):
        print(i*j)

my_list= [[i*j for j in range(4,7)] for i in range(6,8)]
print(my_list)

#truthy and falsy values

#truthy values - Non zero numbers, non empty list, tupples, sets
#falsy values- False, None, 0, "" , {} , set(), [], ()


my_list = []
my_list = list()
my_list.append(1)
nested_list = [[1,2] , 3 , 4 ,5]
(a,b), *unused = nested_list

str1= str([1,2,3,4])
a = exec(str1) 
print(a)


a = eval(str1) 
print(a)
print(type(a))

students = {"name": "John", "age": 23, "Subjects": "CompSci"}
print(students["name"])
print(len(students))
print(students.keys())
print(students.values())
print(students.items())


print(list(filter(lambda x: x != 3, [1, 2, 3, 4])))
print(list(filter(lambda x: x%2==0, [1, 2, 3, 4])))

list_input = input("Enter a list")
my_list = list_input.split()


my_list = map(lambda n : n*n, nums) 
print(list(my_list))


my_evenlist = filter(lambda n: n%2==0, nums)
print(list(my_evenlist))
