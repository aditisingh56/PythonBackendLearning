#  no we will do two dimensional list
#  a two dimensional list is a list of lists. It is a list that contains other

#  its indexing is as list[row][column]
two_dimensional_List = [
    [1 ,2 ,3],
    [4, 5, 6],
    [7, 8 ,9]
]
print("We can print two dimensional list by using nested loops")
for row in two_dimensional_List: # this will acess each row of the two dimensional list one by one like [1, 2, 3] then [4, 5, 6] and then [7, 8, 9], here row is a variable that will take the value of each row one by one
    for col in row:  # this will acess each column of the row one by one like 1 then 2 then 3 and then 4 then 5 then 6 and then 7 then 8 and then 9
        print(col)

print(two_dimensional_List)

#  if we want to acces any specific element of the two dimensional list we can do it by using its index like this

print(two_dimensional_List[0][0]) # this will print 1 which is the element at index 0,0

print(two_dimensional_List[1][2])  # this will print 6 which is the element at index 1,2

#  lets me exaplin the for row in two_dimensional_List: # this will acess each row of the two dimensional list one by one like [1, 2, 3] then [4, 5, 6] and then [7, 8, 9], here row is a variable that will take the value of each row one by one
    # for col in row:  # this will acess each column of the row one by one like 1 then 2 then 3 and then 4 then 5 then 6 and then 7 then 8 and then 9
    #     print(col)
    #  here whta actually happens is , we dont want to print just one row here, if we wanted to we could have done it by using its index like this print(two_dimensional_List[0]) which will print [1, 2, 3] or using single loop like this for row in two_dimensional_List: print(row) which will print [1, 2, 3] then [4, 5, 6] and then [7, 8, 9], but we want to print each element of the two dimensional list one by one so we have to use nested loops, the outer loop will acess each row of the two dimensional list one by one and the inner loop will acess each column of the row one by one and print it.
    # the outer loop will acces the value the inner loop ei;; print that value and then we will go to next row 