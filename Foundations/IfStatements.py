# if sttaement is a control flow statement that allows us to execute a block of code only if a certain condition is true. It is used to make decisions in our code and can be used in various ways, such as with else and elif statements.
#  it is sued to check a condition and execute a block of code if the condition is true. If the condition is false, the block of code will be skipped and the program will continue to the next line of code.


#  eg if a number is divisible by 2 then it is even 
number = 20
if (number %2 ==0):
    print(f"{number} is even")
else:
    print(f"{number} is odd")  # this will run only if the condition in the if statement is false which means the number is not divisible by 2 and hence it is odd

#  we can also do taking input 
number = int(input("Enter a number: "))
if (number %2 ==0):
    print(f"{number} is even")
else:
    print(f"{number} is odd")  # this will run only if the condition in the if statement is false which means the number is not divisible by 2 and hence it is odd

#  we can have a traffic light system using if statement
light_color = input("Enter the traffic light color (red, yellow, green): ")
if light_color == "red":
    print("Stop")
elif light_color == "yellow":  #when we use this means when athe if sttaement is false we will go and execute elif statemnt 
    print("Get ready")
else:
    print("Go")

age = int (input("Enter your age: "))
if (age>=18):
    print("You are eligible to vote")
elif(age<18):
    print("You are not eligible to vote")
else:
    print("Invalid input")

