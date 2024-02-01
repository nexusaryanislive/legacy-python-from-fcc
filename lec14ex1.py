# WAP which repeatedly reads numbers until the user enters done. Once done is entered, print total, count and the average of the numbers. If the user enters anything other than a numeric value, detect their message and skip to the next number

count = 0
total = 0

# Loop mechanism
while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break  # exit mechanism
    # Error prevention mechanism
    try:
        inp = float(inp)
        count = count + 1
        total = total + inp
    except:
        print("Enter a valid numerical")
        continue  # exit mechanism


if count > 0:
    print(f"The total entries are: {count}")
    print(f"The sum of the entries is: {total}")
    print(f"The average of the entries is: {total/count}")
else:
    print("No digit was entered")
