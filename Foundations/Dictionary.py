# di tionary yopu can imagine like a real life dictionary where we have words and their meanings, in python we have a data structure called dictionary which is used to store data in key value pairs. It is also known as associative array or hash map in other programming languages. In python, dictionaries are defined using curly braces {} and the key value pairs are separated by a colon : and each key value pair is separated by a comma ,.
#  key can be anything like a string, number, tuple, etc. but it must be unique and immutable. Value can be anytihng like a string, number, list, tuple, dictionary, etc. but it can be duplicate and mutable.
#  example of a dictionary

student = {
    "name" : "Aditi_Singh" , 
    "age" : 20, 
    "Roll_no" : 12345,
    "Marks" : {
        "Maths" : 90,
        "Science" : 95,
        "English" : 85
    }
}

#  now we will see how tyo acces these 
Student_name = student["name"] # this will give us the value of the key "name" which is "Aditi_Singh"
print(Student_name) # this will print the value of the key "name" which is "Aditi_Singh"
#  we can alos acces with the help of get() method
Student_age = student.get("age") # this will give us the value of the key "age" which is 20
print(Student_age) # this will print the value of the key "age" which is 20

#  now we will acces th dictionary hich is indioe the mau dictiopnary 
#if i want to acces the marks of maths then i can do it by using the key "Marks" and then the key "Maths"
Maths_marks = student["Marks"]["Maths"] # this will give us the value of the key "Maths" which is 
print(Maths_marks) # 

#  we can add new key susing the assignment operator =
student["Class"] = "12th" # this will add a new key "Class" with the value "12th" to the dictionary student
print(student) # this will print the updated dictionary with the new key "Class" and its value "12th"