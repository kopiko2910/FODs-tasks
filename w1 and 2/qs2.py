#this program takes input and does Addition,Subtraction, Multiplication, Division, Modulo division and Floor division

a = float(input("Enter a number: "))
b= float(input("Enter another number: "))
add = a+b
sub = a-b
mul = a*b
if b!=0:
    div = a/b
    mod_div = a%b
    floor_div=a//b
else:
    div = "undefined"
    mod_div = "undefined"
    floor_div = "undefined"
print("\nRESULTS:")
print("1) The Addition of ",a ,"and",b ,"= ", add )
print("2) The Subtraction of ",a ,"and",b ,"= ", sub )
print("3) The Multiplication of ",a ,"and",b ,"= ",mul )
print("4) The Division of ",a ,"and",b ,"=",div )
print("5) The Modulo Division of ",a ,"and",b ,"= ",mod_div )
print("6) The Floor Division of ",a ,"and",b ,"= ",floor_div )