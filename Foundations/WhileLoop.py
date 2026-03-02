#   a while loop is jab tak , it means jab tak tghis condition is true it will be runnin g.

#  so we shpuld neevr run a loop which does not hasve  astopping condiiton 
#  its syntax is 
# while condition:
#     block of code to be executed

#  now we will write a simple while loop 
a = 10
while(a >0):
    print(a) # this will print the value of a which is 10, 9, 8, 7, 6, 5, 4, 3, 2 and 1
    a = a -1 # this will decrease the value of a by 1 in each iteration of the loop

print("In this loop , a will be printed 10 times")

#  we can do this by taking user input to
n = int (input("Enter a number: "))
while( n > 0):
    print(n) 
    n = n - 1
#  tjhis will do the same woek 

#  let ius print table of n now, whose input we already took 
print('The multiplication table of this is: ')
number = int(input("Enter a number: "))
i =1
while( i <=10):
    print(number * i)
    i+=1

# now we will print factorial ogf this n 

factorial = 1 
i =1
while(i <= number):
    factorial = factorial * i
    i+=1
print(factorial)