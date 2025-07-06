#this program performs the given equation given the value oa a, b and c
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
resulta = a**2 + 2*a*b + b**2
resultb = a**5 + 2*a*b*c + b**3 + c**4
resultc = a**7 + 5*(a**3)*(b**2)*(c**6) + b**7
print("\nResults:")
print("I. a² + 2ab + b² =", resulta)
print("II. a⁵ + 2abc + b³ + c⁴ =", resultb)
print("III. a⁷ + 5a³b²c⁶ + b⁷ =", resultc)
