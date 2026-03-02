# x = int (input("Enter an number: "))
# print(x)
# print("If  the number i enter is not an number , the program eill give error , and an errror is a bad sign of a programmer")
#  to avoid this we can use error handling and error correction in python

try:
    x = int (input("Enter an number: "))
    print(x)
except ValueError: # this will catch the error if the user enters a value that is not an number and will print the message "Invalid input, please enter a number"
    print("Invalid input, please enter a number")
else:
    print("No error occurred") # this will run only if there is no error in the try block
finally:
    print("This will always run") # this will run no matter what, whether there is an error or not in the try block

#  try block : code that may have error whrn we run
# except block , catches the error that is raised in try block, it is better if we sopecify the type of error 
# else block contains code that will run if there is no errro that is catched in the except block, this is els efor except block 
# finally block contains code that will run no matter what, whether there is an error or not in the try block, this is for both try and except block

#  valueError : it is the eror thta is raised when we try to convert a value that is not an number to an number using int() function, for example if we enter "abc" instead of a number, it will raise a ValueError
#  name error : it is the error that is raised when we try to use a variable that is not defined, for example if we try to print a variable that we have not defined, it will raise a NameError eg if we write print x and x is not defined it will raise a NameError
#  type error : it is the error that is raised when we try to perform an operation on a value of a type that is not supported, for example if we try to add a string and an number it will raise a TypeError eg if we write "abc" + 5 it will raise a TypeError
# zero division error : it is the error that is raised when we try to divide a number by zero, for example if we write 5/0 it will raise a ZeroDivisionError

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1/number2
    print(result)
except ValueError:
    print("Invalid input, please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error occurred")
finally:
    print("This will always run")
    
