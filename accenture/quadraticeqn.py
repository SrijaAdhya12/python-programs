def find_roots(a,b,c):

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (- b + d**0.5) /( 2*a)
        x2 = (- b - d**0.5) / (2*a)
        return x1,x2
    if d == 0:
        x1 = -b/(2*a)
        x2 = -b/(2*a)
        return x1,x2
    else:
        return "No real roots"

    




a = int(input())
b = int(input())
c = int(input())
print(find_roots(a,b,c))