def Celsius_to_Fahrenheit(Celsius):
    """ calculation from C to F """
    Fahrenheit = Celsius * (9/5) + 32
    return Fahrenheit


def Fahrenheit_to_Celsius(Fahrenheit):
    """ calculation from F to C """
    Celsius = (Fahrenheit - 32) * (5/9)
    return Celsius

c = 30
print(c, "degree of °C is", Celsius_to_Fahrenheit(c), "°F")

f = 60
print(c, "degree of °F is", Fahrenheit_to_Celsius(f), "°F")

print("Transfer to °F then transfer back", Fahrenheit_to_Celsius(Celsius_to_Fahrenheit(40)))
