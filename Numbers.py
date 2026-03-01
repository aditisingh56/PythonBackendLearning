print(77) #we can print numbers in python without using quotes
# python is a dynamically typed language which means we do not need to declare the type of variable before using it, we can directly assign a value to a variable and python will automatically detect the type of variable
number = 77 # we can assign a number to a variable and then we can use that variable to print the number
print(number) # this will print the value of the variable number which is 77
print(type(number))
""" we can also perform many opertaion s with numbwrs like
"""
# addition
a = 10
b = 20
print(a + b) # this will print the sum of a and b which is 30
# subtraction
print(a - b) # this will print the difference of a and b which is -10
# multiplication
print(a * b) # this will print the product of a and b which is 200
# division
print(a / b) # this will print the quotient of a and b which is 0.5
# modulus
print(a % b) # this will print the remainder of a and b which is 10
# exponentiation
print(a ** b) # this will print the value of a raised to the power of b which is 100000000000000000000
# w ecn also print negative numbers
print(-a) # this will print the negative value of a which is -10
#  we can also use absolute value function to get the absolute value of a number
print(abs(-a)) # this will print the absolute value of -a which is 10 
#  we can also fidn max and min 
print(max(a, b)) # this will print the maximum value between a and b which is 20
print(min(a, b)) # this will print the minimum value between a and b which is 10
#  there are som emethods to use them we need to import the math module
from math import *
print(sqrt(16)) # this will print the square root of 16 which is 4.0
#  poiny to remeber is srt function returns a float value even if the input is a perfect square