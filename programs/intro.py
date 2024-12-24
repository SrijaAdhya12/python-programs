# import my_module
# import my_module as mm
# from my_module import *
# from programs.my_module import find_index, test
import random
import math
import datetime
import calendar
import os

courses = ["History" , "Math" , "Physics" , "ComputerSci"]

# index= find_index(courses , "Math")
# print(index)
# print(test)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())