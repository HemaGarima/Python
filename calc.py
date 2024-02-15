# import module2

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# print("Addition" , module2.add(num1,num2))
# print("Subtraction" , module2.sub(num1,num2))
# print("Multiplication" , module2.mul(num1,num2))
# print("Division" , module2.div(num1,num2))


# ALIAS

# import math as m

# print("Square root of 36 : " , m.sqrt(36))
# print("3 to the power of 4 : " , m.pow(3,4))

# IMPORT FROM MODULE

# from module2 import add,sub

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# print("Addition" , add(num1,num2))
# print("Subtraction" , sub(num1,num2))

# IF WE WANT TO IMPORT EVERYTHING FROM A MODULE BUT WE DO NOT NEED TO PREFIX MODULE NAME AGAIN AND AGAIN

# from module2 import *

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# print("Addition" , add(num1,num2))
# print("Subtraction" , sub(num1,num2)) 
# print("Multiplication" , mul(num1,num2)) 
# print("Division" , div(num1,num2)) 

# dir() FUNCTION

from operator import mod
import math
lst1 = dir(math)
print(lst1)