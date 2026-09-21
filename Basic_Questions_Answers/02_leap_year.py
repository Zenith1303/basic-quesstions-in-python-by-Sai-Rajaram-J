year = int(input("Enter a positive year: "))
if year <= 0:
    print("Please enter a positive year.")
elif year % 400==0 or (year%4==0 and year%100!=0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
