#  so jab hum parent class se uske properties aur methods use karte hai without rewritting the same , it is called imnherting 
# inheritance we can use with other file too, when oin eclass is one file , we can us ethat class metyhods andf propeerties in another class.
#  we can do tyhis by using  from fileName import className

#  now we will see inheritance 

# class Animal:
#     def eat(self): #this self here is, so that it can tell ki this object. it is like a reference to the object that is calling the method, it is used to access the properties and methods of the class in which it is defined, it is used to differentiate between the properties and methods of the class and the local variables and parameters of the method
#         print("This animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("The dog is barking")
# d = Dog()
# d.eat() # this will call the eat method of the Animal class because the Dog class is inheriting from the Animal class
# d.bark() # this will call the bark method of the Dog class because the Dog class has its own method called bark


# now we w ill see contructor in inheritence 

class animal:
    def __init__(self , name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating") # here, self.name is used to access the name property of the animal class, it is used to differentiate between the name property of the animal class and the name parameter of the __init__ method
class dog(animal):
    def __init__(self , name , breed):  # we shpuld use pehla ka parameter toothis is deffining this method, we have not used super yet. 
        super().__init__(name) # this will call the __init__ method of the animal class and pass the name parameter to it, so that we can access the name property of the animal class in the dog class, super() is
        self.breed = breed
d = dog("Buddy", "Golden Retriever")
print(d.name) 
print(d.breed)

# self is used, to access the properties and methods of the class in which it is defined, it is used to differentiate between the properties and methods of the class and the local variables and parameters of the method, it is a reference to the object that is calling the method, it is used to access the properties and methods of the class in which it is defined, it is used to differentiate between the properties and methods of the class and the local variables and parameters of the method

#  super is used to call the methods of the parent class, its syntax is 
#  superdotmethodname(parameters)
#  eg: super().__init__(name) 
#  or super().dog(breed)