#this program calculates square and square root of the nuber, exponent value, log base 10, and power 3,4 and 5 of the number
import math
a = float(input("Enter a number: "))
square = a ** 2
square_root = math.sqrt(a)
exponent = math.exp(a)
log_base10 = math.log10(a)
power3 = a ** 3
power4 = a ** 4
power5 = a ** 5
print("\nResults:")
print("I. The Square of", a, "is:", square)
print("II. The Square root of", a, "is:", square_root)
print("III. The Exponent value (e^"+str(a)+") is:", exponent)
print("IV.The Log Base 10 of", a, "is:", log_base10)
print("V. The Powers of", a)
print( a, "^3 =", power3)#" -" creates an indented bullet point (3 spaces and a hyphen)
print( a, "^4 =", power4)
print( a, "^5 =", power5)
