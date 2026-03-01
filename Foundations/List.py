fruits = [ "Apple" , "Banana" , "Cherry" , "Date" , "Elderberry" ]
# now if i want to print the first fruit in the list i can do it by using index
print(fruits[0]) # this will print the first fruit which is Apple

# if i wnat to print all the fruits
print(fruits)
#  i can also print specific fruits
print(fruits[1:4]) # this will print the fruits from index 1 to 3 which are Banana, Cherry and Date
#  i can alos prin t two different fruits
print(fruits[0], fruits[3]) # this will print the first and fourth fruit which are Apple and Date

# i can alos understand what type of data is stored in the variable fruits
print(type(fruits))
 # this will print the type of data stored in the variable fruits which is list
#   i can directly egt the lat value as 
print(fruits[4])

# theres anoyher wayu also to do it , using -1
print(fruits[-1]) # this will also print the last fruit which is Elderberry and 
#  -2 will give us the second last fruit which is Date

print (fruits[-2]) 

#  we can get lengtrh of the list too

print (len(fruits)) # this will print the length of the list which is 5
#   i can also have different ata types in a list  alist is a :
""" 1-Mutuable
2-Ordered
3-Allows duplicate elements
4-Allows different data types"""

#  we can find the type of the list elements 
elemnets = [1, "Aditi", 3.14, True]
t = type(elemnets[0])
print(t) 

#  there is another way of craetimng a list using the list() function
#  example
print("List in different way")
numbers = list((1, 2, 3, 4, 5))  # ptr is here we need to use two rounded brackets, one becausee we are suing function loist and anothe rbeacuse we are passing a tuple as an argument to the list function 
print(numbers) 
print(type(numbers))