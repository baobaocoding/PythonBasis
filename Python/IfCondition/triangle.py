import math


def isTriangle(a, b, c):
    """ check if it is a triangle (return True or False) """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


def calcTringle(a, b, c):
    """ calculate a tringle's perimeter and area """
    perimeter = a + b + c
    area = math.sqrt(perimeter * (perimeter - a) *
                     (perimeter - b) * (perimeter - c))

    return perimeter, area


def calculate(candidate):
    """ as main function for the candidates """
    if isTriangle(*candidate):
        perimeter, area = calcTringle(*candidate)
        print("The perimeter of this triangle is",
              perimeter, "and the area is", area)
    else:
        print("This is not a triangle.")


candidate1 = [3, 4, 5]
candidate2 = [1, 2, 3]
calculate(candidate1)
calculate(candidate2)
