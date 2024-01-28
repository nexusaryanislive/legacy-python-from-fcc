# WAP to calculate the apy of an employee, and if the work time is more than 45 hrs, they receive an overtime i.e 1.5 the salary

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

#  Regular vs Ot
if hrs <= 40:
    reg_pay = hrs*rate
    try:
        reg_pay = int(reg_pay)
        print("You have worked as regular time.\nThe total pay is: $", reg_pay)
    except:
        reg_pay = -0
        print("Pay could not be computed")
        print("The total pay is: $", reg_pay)

else:
    ot = (hrs*rate) + (hrs-40.0)*(0.5*rate)
    try:
        ot = int(ot)
        # Note the syntax for adding a variable in between a sentence below
        print(f"You have worked {hrs-40.0} hrs overtime.")
        print("Appreciate your commitment!!\nYour total pay is: $", ot)
    except:
        ot = -1
        print("Pay could not be computed")
        print("The total pay is: $", ot)
