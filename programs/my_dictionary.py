# dictionaries
students = {"name": "John", "age": 23, "Subjects": "CompSci"}
print(students["name"])
print(students["Subjects"])
students = {"name": "John", "age": 23, "Subjects": "CompSci"}
print(students.get("name"))
students["phone"] = "9999"
print(
    students.get("phone", "not found")
)  # second argument is the default value when a key is not found
students["name"] = "Jane"
print(students)

students.update({"name": "Srija", "age": 26})
print(students)

print(len(students))
print(students.keys())
print(students.values())
print(students.items())
# age = students.pop('age')
# print(age)
# print(students)

for key, value in students.items():
    print(key, value)
