# def greet() -> None:
#     print('Hello World')

# def bye() -> None:
#     print('Bye World')


# def main() -> None:
#     greet()
#     bye()

# if __name__ == '__main__':
#     main()


def is_an_adult(age:int, has_id:bool) -> bool:
    return age >= 21 and has_id

def is_bob(name:str) -> bool:
    return name.lower() == 'bob'

def enter_club(name:str, age:int , has_id:bool) -> None:
   if is_bob(name):
       print('Get out of here!')
       return
   if is_an_adult(age, has_id):
       print('Welcome to the club!')
   else:
       print('You are not allowed to enter the club')

def main() -> None:
    enter_club('bob', 21, True)
    enter_club('James', 29, False)
    enter_club('Sandra', 23, True)
    enter_club('Mario', 20, True)

if __name__ == '__main__':
    main()


