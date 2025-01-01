"""Default Constructor: A default constructor has only one argument self and used to initiate objects with default value"""

class Student:
     name= "Srija"
        
student = Student()
print(student.name)

"""One Argument: A constructor with one argument, allows to set specific value"""

class Student1:
    def __init__(self,name):
        self.name = name
        
student1 = Student1("Srija")
print(student1.name)

"""Multi Argument: A constructor with multiple arguments"""

class Student2:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    
student2 = Student2('Srija', 21, 'Kolkata')
print(student2.name)
print(student2.age)
print(student2.city)