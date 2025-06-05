import math

def hiring_car(r1, n, r2, x):
    total_hours = math.ceil(x/60)
    if total_hours <= n:
        cost = r1*n
    else:
        cost = r1*n + (r2*(total_hours-n))
    return cost

r1, n, r2, x = 20, 4, 40, 300
print(hiring_car(r1, n, r2, x))

