print("Create your account:")

username = input("Input username: ")
password = input("Input password: ")

print(" Your Account has been created succesfully!")
print("Login now!")

username2 = input("Input username: ")
password2 = input("Input password: ")

if(username == username2 and password == password2):
    print("Login successful!")
else:
    print("Login failed! Please check your username and password and try again.")