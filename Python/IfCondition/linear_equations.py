def f(x):
    if x > 1:
        y = 3 * x - 5
    elif 1 >= x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    
    return y

x = float(input("Please input a number:"))
print("f(x) is", f(x))