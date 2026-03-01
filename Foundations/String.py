print("hi. How are you? I'm a single line" )
#  if i wsnt to print it in a anew line
print('hi. How are you? \nI am new line.')
# strings can be accesed with index and indexing in  python startes from 0
name = "Aditi"
print(name[0]) # this will print the first letter of the name which is A 

# Mthods of string 
uppercase = name.upper()
lower = name.lower()
print(uppercase) # this will print the name in uppercase which is ADITI
print(lower) # this will print the name in lowercase which is aditi
print (name.isupper())

# Replacing 
new_name = name.replace("A", "E")
print(new_name) # this will replace the A with E and print the new name which is Editi
print (name)  # this will print the original name which is Aditi because the replace method does not change the original string it creates a new string with the changes