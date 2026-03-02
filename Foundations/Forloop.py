# for loop is used to loop through a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. It is used to iterate over a sequence of items and perform a specific action for each item.
#   its keyword is for 
#  its syntax is
# for variable in sequence:
#     block of code to be executed

list = [ "fruits" , "Sportts" , 4 ,78 , "age"]
for items in list:
    print(items) # this will print each item in the list one by one

print("This will iterate through each value of the ")

#  we can also print in soe range 
for i in range(1, 11):
    print(i) # this will print the numbers from 1 to 10
print("This will print the numbers from 1 to 10")

#  there is break and continue two keywords that we can use in for looo 

# break 0- works like a full stop
for i in range (2,10,2):
    if i == 6:
        break # this will stop the loop when i is equal to 6
    print(i) # this will print the even numbers from 2 to 8

print("This will print the even numbers from 2 to 8")

# continue - works like a comma
for i in range (2,10,2):
    if i == 6:
        continue # this will skip the iteration when i is equal to 6 and continue with the next iteration
    print(i) # this will print the even numbers from 2 to 8 except 6
print("This will print the even numbers from 2 to 8 except 6")