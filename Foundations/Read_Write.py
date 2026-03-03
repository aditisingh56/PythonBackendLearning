#  now we can open the file in two different way ek 

#  y = open("test.txt", "r")  #  read mode
#  here we have to xlos eit like this y.close()

# and another way of doing was, with open("test.txt", "r") as y:  #  read modeaise , when we use with we dont have to close it 

# with open("Foundations/Writingfile.txt" , "r") as f: # we are inside pythonbackend follder , we need t nav8hate inside fundation folder and then do this 
#     content = f.read()
#     print(content)

#     # we can also check if a file is readable or not by using the isreadable() method
# #  now we will try to append something , which means wriote something at the end og the file

# with open("Foundations/Writingfile.txt" , "a") as f: # we are inside pythonbackend follder , we need t nav8hate inside fundation folder and then do this
#     f.write("\nThis is a new line") # this will write this line at the end of the file, we can see the change in the file after running this code

# a - append mode, it will add the new content at the end of the file without overwriting the existing content
#  w - write mode, it will overwrite the existing content of the file with the new content, if the file does not exist it will create a new file with the given name and write the content in it
#  r - read mode, it will allow us to read the content of the file, if the file does not exist it will raise a FileNotFoundError
#  r+ - read and write mode, it will allow us to read and write the content of the file, if the file does not exist it will raise a FileNotFoundError
#  w+ - write and read mode, it will allow us to write and read the content of the file, if the file does not exist it will create a new file with the given name and write the content in it, if the file already exists it will overwrite the existing content of the file with the new content and then we can read the content of the file
#  so if files do not exist, the modes that will create a new file are w, w+ and a, if the file already exists, the modes that will overwrite the existing content of the file are w and w+, the modes that will not overwrite the existing content of the file are a and r+ and r

#  thr modes thst when we use before content will go and new content willcome are a and w, when we use a the new content will be added at the end of the file without overwriting the existing content, when we use w the new content will overwrite the existing content of the file with the new content, if the file does not exist it will create a new file with the given name and write the content in it

# with open("Foundations/Writingfile.txt" , "r") as f: 
#     for i in f:
#         print(i)

with open("Foundations/Writingfile.txt" , "r") as f:
    for i in f:
        print(i)
       