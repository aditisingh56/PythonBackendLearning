list1 = [1, 2, 3, 4, 5]
list2 = ["Aditi", "Python", "Programming"]
list1.extend(list2) # this will extend list1 with the elements of list2
print("Appending value")
list2.append("New value") 
print("Adding at specific position ")

list1.insert(2, "Inserted value")

print(list1)
print("Finding the element")
print(list1.index("Inserted value")) # this will print the index of the element "Inserted value" which is 2

print("Removing something")
list1.remove("Inserted value") # this will remove the element "Inserted value" from the list