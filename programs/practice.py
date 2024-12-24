# # Strings:

# message = "Hello world is helloworld"

# print(message.lower())
# print(message.upper())
# length= len(message)
# print(message[:length-1])
# print(message.count("world")) #count the presence of anything in our string
# print(message.count("o")) #count the presence of "o" in our string
# print(message.find("o")) #find index
# var= message.replace("Hello", "*")
# print(var)
# greeting="Hi"
# name="srija"
# message= f'{greeting}, {name} welcome'
# print(message)

# # int and floats
# print(round(1.23))
# print(round(2.7345 ,2))

# lists

courses = ['History' , 'Maths' , 'Physics']
courses2= ["Chemistry" , "EVS"]
print(len(courses))
courses.insert(0 , "Art")
print(courses)
courses.append(courses2) #appendn adds the entire list to another list, creates a nested list
print(courses)
courses.extend(courses2) #extends adds the items of courses 2 in courses 1
print(courses)
courses.remove("Maths")
print(courses)

popped = courses.pop()
print(popped)
print(courses)

# print(courses[::-1])
list1 = ["Srija" , "Pritam" , "Golu"]
list1 = ["Srija" , "Pritam" , "Golu"]
courses.reverse()
print(courses)
list1.sort()
print(list1)
list1.sort(reverse=True) #sorts in decending order
print(list1)
sorted_courses = sorted(list1) #returns sorted list in a new list
print(sorted_courses)

num_list= [6,1,7,9,5]
print(min(num_list))
print(max(num_list))
print(sum(num_list))
print(num_list.index(9))

for i,value in enumerate(num_list , start=1):
    print(i,value)


str_list= ["hello" , "hii" , "byee"]
print(str_list.count("hello"))
course_str= "_ ".join(str_list)    
print(course_str)
new_list = course_str.split(" ")
print(new_list)

#mutable_example:
list1= [3,5,1,2,3]
list1[0]=2
print(list1)

#tupples (immutables)

# tuple1= ("History" , "Maths" , "Physics")
# tuple1[0]="geo"
# print(tuple1)


#Sets (No duplicates)

cs_courses = {'history' , 'Math' , 'Physics' , 'CompSci'}
art_courses = {'history' , 'Design' , 'Physics' , 'Polity'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_set = {} #!its a dictionary
empty_set = set()