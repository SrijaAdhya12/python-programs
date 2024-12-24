a, b = 8, 3  # unpacking a tuple
if a < b:
    print("a is lesser than b")
elif a > b:
    print("b is lesser than a")
else:
    print("a and b is equal")

# if
# n<1 ? "true" : null
# syntax: true_condition if condition else None
print("a is lesser than b") if a < 1 else None

# if_else
# n<=1 ? "true" : "false"
# syntax: true_condition if  condition else false_condition


print("a is lesser than b" if a < b else "a and b is equal")

# if_elif_else
# n<=1 ? "true" :(n>b ? "false" : "false")

# Syntax:if_condition if condition else (elif_condition if condition else else_condition)

print(
    ("a is lesser than b")
    if a < b
    else ("b is lesser than a" if a > b else "a and b is equal")
)


if a < b:
    print("a is lesser than b")
else:
    if a > b:
        print("b is lesser than a")
    else:
        print("a and b is equal")
