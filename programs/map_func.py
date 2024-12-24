def func(a):
    return a**2


my_list = list(range(1,11))
print(my_list)
my_map= list(map(func, my_list)) #map applies a function over an iterable
print(my_map) 


var= lambda a,b,c,d:a+b*c*d


print(var(1,2,3,4))

lambda a:a**2

lambda my_list: my_list[1]

def sec(my_list): return my_list[1] 

lambda my_list, item: my_list.append(item)

lambda sentence: sentence.split(" ")
print((lambda sentence: sentence.split())("Hello World"))
print((lambda sentence: list(sentence))("Hello world"))

lambda greeting : greeting + input("enter your name")
# print((lambda greeting: greeting + " " + input("enter your name: "))("Good Morming"))

my_map= tuple(map(lambda item: item**2 , range(1,11)))
print(my_map)

items = [
    {"name" : "pritam" , "blood_group": "A+" }, 
    {"name" : "srija" , "blood_group": "A+" }, 
    {"name" : "cutu" , "blood_group": "AB+" }, 
]

print(list(map(lambda dic: dic["blood_group"],items)))

# my_list= input().split(",")
# print(list(map(int, my_list)))

students = {
    "Srija" : [90,21,34] 
    
    } 
students["Pritam"] = [76,67,89]


print(students["Pritam"])

for name in students:
    print(name, students[name])

print(list(filter(lambda x: x != 3, [1, 2, 3, 4])))
print(list(filter(lambda x: x%2==0, [1, 2, 3, 4])))
