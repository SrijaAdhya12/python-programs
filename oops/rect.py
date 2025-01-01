class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width  
        
rect1 = Rectangle(20,40)
print(rect1.area())