#method overloading

#using *args

class Calculator:
    def calculate(self, *args):
        if len(args) == 1:
            return args[0] ** 2
        elif len(args) == 2:
            return args[0] + args[1]
        else:
            raise ValueError("Invalid number of argument")

calculator = Calculator()
print(calculator.calculate(2))

class Sumation:
    def sum(self, *args):
        if len(args) == 1:
            return args[0] + args[0]
        elif len(args) == 2:
            return args[0] ** args[1]
        else:
            raise ValueError("Invalid arguments")
            
sums = Sumation()
print(sums.sum(2))
    
#using kwargs

class Greet:
    def greetings(self, **kwargs):
        if 'name' in kwargs:
            return f"Hello {kwargs['name']}"
        elif 'name' in kwargs and 'city' in kwargs:
            return f"Hello {kwargs['name']} and {kwargs['city']}"
        else:
            raise ValueError("Not a valid argument")
        
greeted = Greet()
print(greeted.greetings(name = 'Srija'))
            
        