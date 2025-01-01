
class Microwave:
    def __init__(self, brand, powerrating): #initiate a class
        self.brand = brand
        self.powerrating = powerrating
        self.turned_on = False
        
    def turn_on(self):
        if self.turned_on :
            print("Microwave is turned on")
        else:
            self.turned_on = True
            print("Microwave is already turned on")
            
    def turn_off(self):
        if self.turned_on :
            print("Microwave is turned off")
        else:
            self.turned_on = True
            print("Microwave is already turned on")
            
    def run(self, seconds):
        if self.turned_on:
            print(f'Running {self.brand} for {seconds} seconds')
        else:
            print("Microwave is not turned on")

    def __add__(self, other): #dunder method
        return self.powerrating + other.powerrating
    
    def __str__(self):
        return f"{self.brand} {self.powerrating}"
    
    def __repr__(self): #overrides the default representation of the object
        return f"{self.brand} {self.powerrating}"
        
#self makes sure all the attribute stick to the current instance of a class, its name can be changed       
    
smeg = Microwave('Smeg', 'B') #instance of a class
print(smeg)
print(repr(smeg))
smeg.turn_on()
smeg.run(10)
smeg.turn_on()

bosh = Microwave('Bosh', 'A')
print(bosh.brand)
print(bosh.powerrating)


#dunder methods
print(smeg.powerrating + bosh.powerrating)

# __str__ and __repr__ , str is for user friendly, repr is for developer readable


