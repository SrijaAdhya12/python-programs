def function(): #takes no argument return none
	pass
def function1(): #takes no argument return none
	...
a = 1   

def function2(a): #takes 1 argument return none
	print(a) 


def function3(): #takes no argument returns a string
	return "new string"

def function4(b): #takes one argument returns one
	return b

def my_sum(a,b):
	return a+b

def default_args(arg=0):
	return arg

def default_args2(args=2):
	return args+2
	
def default_args3(item, my_list=[1,2]):
	my_list1 = []
	return my_list.append(item)

# print(function())
# print(function1())
# print(function2(5))
# print(function3())
# print(function4(5))
# print(my_sum(4,6))
# print(my_sum("my name", "  is Srija"))

print(default_args())
print(default_args(5))
print(default_args2())
print(default_args2(5))
print(default_args3(5))