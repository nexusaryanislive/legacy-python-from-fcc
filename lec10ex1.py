# WAP to calculate the apy of an employee, by creating the function called computepay which takes two parameters (hours and rate)

def computepay(hrs, rate):
    if hrs <= 40:
        pay1 = hrs * rate
        return pay1
    else:
        pay2 = hrs*rate + (hrs-40.0)*(rate/2)
        return pay2


try:
    hrs_input = float(input("Enter the man-hours: "))
    rate_input = float(input("Enter the rate per hr: $"))
except:
    hrs_input = 0
    rate_input = 0
    print("Enter a valid numeric")

x = computepay(hrs_input, rate_input)
print("The total pay is: $", x)
