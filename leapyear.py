#Display leap year from the current year to the final yr

"""
import datetime
yr1=datetime.date.today().year
fyr=int(input("Enter the final year:"))
if fyr<yr1:
    print("year must be greater than or equal tro the curremt year")
else:
    print(f"leap year fron {yr1} to {fyr}")
    for year in range (yr1,fyr+1):
        if(year%4==0 and year%100!=0) or (year%400==0):
            print(year)
"""
"""
yr1=int(input("Enter the starting year:"))
yr2=int(input("Enter the ending year:"))
print(f"leap year from {yr1} to {yr2}:")
for year in range(yr1,yr2 + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        print(year)
""" 
