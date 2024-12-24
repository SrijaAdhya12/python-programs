def is_palindrome(num):
    return num == num[::-1]



for i in range(1,101):
    result= is_palindrome(str(i**2))
    if result:
        print(f"{i} is a palindrome and square is {i**2}")
        

