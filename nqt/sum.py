# Sum of the numbers in a string.

def sum_in_string(str):
    sum = 0
    for num in str:
        sum += int(num)
    return sum
        
    

my_str = input("Enter a string on numbers: ")
print(sum_in_string(my_str))

# using sum function


def sum_in_string(str):
    return sum(int(num) for num in str)
    
my_str = input("Enter a string on numbers: ")
print(sum_in_string(my_str))