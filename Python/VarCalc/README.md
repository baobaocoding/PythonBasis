# Python Variable and Basic Calculation

The [Day01](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/01.%E5%88%9D%E8%AF%86Python.md) and [Day02](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/02.%E8%AF%AD%E8%A8%80%E5%85%83%E7%B4%A0.md) content of [Python-100-Days](https://github.com/jackfrued/Python-100-Days#day0115---python%E8%AF%AD%E8%A8%80%E5%9F%BA%E7%A1%80)

## Notes

maybe take some notes here.

## Practice

### 1. Transfer temperature between Celsius (°C) and Fahrenheit (°F)

> [Celsius to Fahrenheit conversion](https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html)

$$
C = (F - 32) \times \frac{5}{9}
$$

$$
F = C \times \frac{9}{5} + 32
$$

```py
def Celsius_to_Fahrenheit(Celsius):
    """ calculation from C to F """
    # code here

    return Fahrenheit

def Fahrenheit_to_Celsius(Fahrenheit):
    """ calculation from F to C """
    # code here

    return Celsius
```

### 2. Calculate circle perimeter and area by radius

$$
L = 2 \times \pi r \\
A = \pi \times r^2
$$

```py
def Perimeter(radius):
    """ calculate perimeter by radius """
    # code here

    return perimeter

def Area(radius):
    """ calculate area by radius """
    # code here

    return area
```

### 3. Check if a year is leap year

* Is a multiple of 4
* But not a multiple of 100
* But can be a multiple of 400

```py
def isLeap(year):
    """ determine if a year is leap year or not """
    # code here

    return is_leap # True or False
```
