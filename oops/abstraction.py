from abc import ABC, abstractmethod

class Computer(ABC): #abstract class must have atleast one abstract method
    @abstractmethod
    def process(self): #abstract method
        pass
        
class Laptop(Computer):
    def process(self): #all abstract methods of abstract class must be defined
        print ("Its runnning")