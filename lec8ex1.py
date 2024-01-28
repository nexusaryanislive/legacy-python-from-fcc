# Use try-except to handle any characters used instead of numericals as input

hrs = input("Enter the man-hours: ")
rate = input("Enter the hourly rate: $")

try:
    hrs = int(hrs)
except:
    hrs = 0
    print("Please enter the hours in numeric, eg. 37, 6.5")

try:
    rate = int(rate)
except:
    rate = 0
    print("Please enter the rate as a numeric data type")

pay = hrs*rate
try:
    pay = int(pay)
except:
    pay = -1
    print("Pay could not be computed")

print("The total pay is: $", pay)
