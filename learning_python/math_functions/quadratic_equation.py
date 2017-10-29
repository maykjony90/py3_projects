from math import sqrt

def quadratic_formula(a, b, c):
    d = (b**2) - (4*a*c)  # discriminant
    print(a, b, c)

    if d < 0:
        print("This equation has no real solution")
    elif d == 0:
        x = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
        print("This equation has one solution: ", x)
        return x
    else:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        print("This equation has two solutions: ", x1, " and", x2)
        return x1, x2
