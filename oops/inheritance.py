class A: #super class
    def feature1(self):
        print("Feature 1 is working")
        
    def feature2(self):
        print("Feature 2 is working")
        
class B (A): #sub class, single level inheritance
    def feature3(self):
        print("Feature 3 is working")
    
    def feature4(self):
        print("Feature 4 is working")
        
class C (B): # Multilevel inheritance
    def feature5(self):
        print("Feature 5 is working")
 
       
b1 = B()
c1 = C()
print(c1.feature4())
print(b1.feature3())