#  to define  afunction we use the keyword def
def greetings():
    print("Hello, welcome to Python programming!") #here, in python indentattion is very imprtotant we start after 4 gaps 

#  we can call this function by its name 
greetings()
  # this will call the function greetings and print the message "Hello, welcome to Python programming!"
#   we can pass parameters , its when we are deffining it ND ARguments are which when we are acllin ghit 

def print_name( name): # this is an parameter s
    print(f"Hello , {name}!")

name = input("Enter your name: ")
print_name(name)  # this is an argument  

#  we can also pass default paramerters , when we dont pass an argument it will consider that pareameter a sarguemnt 

def print_name(name = "Aditi"):
    print(f"Hello , {name}!")
print_name() # this will print "Hello, Aditi!" because we have not passed any argument so it will consider the default parameter as the argument

# we can also perform concatenation 
def concatenate_strings(string1, string2):
    return string1 + " " + string2

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
fullName = concatenate_strings(firstName, lastName)
print(f"Your full name is: {fullName}")

# when w e dont know how many arguments we want to pass we can use *args and **kwargs
# this means that we can pass any number of arguments and it will be stored in a tuple or a dictionary respectively

#  ptr is it will consider it tuple or dictionary we can pass any number of arguments and it will be stored in a tuple or a dictionary respectively

def print_all(*names):
    print("Welcome : ", names)
names = ("Aditi", "Rohit", "Sonia")
print_all(*names) # this will print "Welcome :  ('Aditi', 'Rohit', 'Sonia')" because we have passed three arguments and it will be stored in a tuple

#  and if we want to print only specific
print("Only specific")
print_all(names[1]) # this will print "Welcome :  Rohit" because we have passed three arguments and it will be stored in a tuple and we are printing the second argument which is Rohit