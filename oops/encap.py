#encapsulation

class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
        
    def set_speed(self, speed):
        self.__speed = speed
        
    def set_color(self, color):
        self.__color = color
        
    def get_speed(self):
        return self.__speed
    
    def get_color(self):
        return self.__color


ford = Car(100, 'red')
ford.set_speed(250)
print(ford.get_speed())
ford.set_color("Red")
print(ford.get_color())


# __ is used to make attribute private
