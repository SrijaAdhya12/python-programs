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

class sumation:
    def sum(self, *args):
        if len(args) == 1:
            return args[0] + args[0]
        elif len(args) == 2:
            return args[0] ** args[1]
        else:
            print("Invalid arguments")
            
sums = sumation()
print(sums.sum(2))
    
        