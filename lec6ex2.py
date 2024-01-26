# Write a programme ttom prompt the user for hours and rate per hour to computegross pay

hours = int(input("Enter the no. of hours: "))
rate = int(input("What is the rate per hr?: $ "))
pay = hours*rate
gross_pay = str(pay)
print("The gross pay is: $"+gross_pay)
