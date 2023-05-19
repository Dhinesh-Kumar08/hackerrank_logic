# to find leap or not
#using boolean and function
def is_leap(year):  
    leap=False,"it is not leap year"  
    if (year % 4 == 0):
        leap = True,"it is leap year"
    return leap


year = int(input("Enter the year :"))
print(is_leap(year))