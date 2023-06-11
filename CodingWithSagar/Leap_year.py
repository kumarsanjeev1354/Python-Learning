#Taking input from user
year=int(input("Please enter year"))
#Check if entered year is a leap year of not
if (year%4==0) or(year%100!=0) and (year%400==0):
    print("Leap year")
else:
    print("not a leap year")