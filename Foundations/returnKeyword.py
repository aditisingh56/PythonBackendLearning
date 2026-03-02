# return ststement is used to exit a function and return a value to the caller. It can be used to return any type of data, including numbers, strings, lists, tuples, dictionaries, etc.
def add(a, b):
    return a + b # this will return the sum of a and b to the caller
num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2) # this will call the add function and pass num1 and num2 as arguments and store the returned value in the variable result
print(f"The sum of {num1} and {num2} is: {result}") # this will print the result which is the sum of num1 and num2309
