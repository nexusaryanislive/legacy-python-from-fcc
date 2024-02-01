# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence: 0.8475 '

x = str.find(':')
str_1 = str[x+1:]
str_2 = float(str_1.strip())
print(f"The string req is:{str_2}")
print(type(str_2))
# print("But we require the digits as float type data")

# str_3 = float(str_2)
# print(f"The float required is:{str_3}")
# print(type(str_3))
