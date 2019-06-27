def isLeap(year):
    """ determine if a year is leap year or not """
    
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0   

    return is_leap # True or False

year = int(input("Please input the year:"))
if isLeap(year):
    print(year, "is leap year.")

else:
    print(year, "is not leap year.")
