# CODE: WAP that takes input of user's age by prompting him and using a function to check for invalid age if age is lesser than 0. Return eligigible as a string if age is greater than or equal to 18 and ineligible if lesser than 18


def is_eligible(age):
    if age>=18:
        return "eligible"
    elif age<0:
        return "invalid age"
    else:
        return "not eligible"

def is_eligible(age):
    return ("eligible" if age>=18 else "invalid age" if age<0 else "not eligible") + "1"


def is_eligible(age):
    if age >= 18:
        return "eligible"
    if age < 0:
        return "invalid age"
    return "not eligible"


# age = int(input("Enter age"))
# print(is_eligible(age))


print(is_eligible(int(input("Enter age"))))
