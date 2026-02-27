import math

firstx = int(input("Enter the first x: "))
firsty = int(input("Enter the first y: "))
secondx = int(input("Enter the second x: "))
secondy = int(input("Enter the second y: "))

print("Distance is : " , (  math.sqrt(  ((secondx-firstx)**2) + (secondy-firsty)**2) ) )
