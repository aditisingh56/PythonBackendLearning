#  classes are the blueprint of the objects. 

#  objects are real world entity 

#  eg of thjem is 
#  syntax:
# class className:
#     # class body 
 
# class Car:
#     def name(name , time):
#         print(f"The name of the car is {name} and it takes {time} hours to reach the destination")
# #  here we have defined a class called Car and a method called name which takes two parameters name and time and prints the name of the car and the time it takes to reach the destination
# #  now we will see , how we have to create objects
# car1 = Car() 

# car1.name("Toyota", 2)

#  now we will see , how we should  cfreate a init class
class Student:
    def __init__(self , name , roll_no):
        self.name = name
        self.roll_no = roll_no
    
objrect1 = Student("Aditi", 123)
print(objrect1.name) 
print(objrect1.roll_no)