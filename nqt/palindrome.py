# Check if a given string is palindrome or not.

def check_palindrome(my_str):
    if my_str == my_str[::-1]:
        return f"{my_str} is a palindrome"
    return "Not palindrome"


my_str = input("Enter a string: ")
print(check_palindrome(my_str))