yr = int(input("enter the year: "))

if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print(f"{yr} this year is a leap year.")
else:
    print(f"{yr} this year is not a leap year.")