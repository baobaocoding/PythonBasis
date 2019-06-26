import math

def Perimeter(radius, pi):
    """ calculate perimeter by radius """
    
    perimeter = 2 * radius * pi

    return perimeter

def Area(radius, pi):
    """ calculate area by radius """
    
    area = radius ** 2 * pi

    return area

r = float(input('Please input radius:'))
pi = math.pi 

print("Perimeter is:", Perimeter(r, pi))
print("Area is: %f" % Area(r, pi))
