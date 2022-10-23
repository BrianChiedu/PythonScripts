
def list_of_list_generator_modified(n):
    #Create an empty list
    lst5 = []
    #We loop through each number up to n. N is the number passed into the function
    for i in range(n):
        # on the first iteration we create a new list that has the current i plus 1 and add it to to our empty list
        if i == 0:
            lst5.append([i+1])
        # on all iterations after that we first unpack the previous list then add the current i plus 1 to our empty list
        else:
            lst5.append([*lst5[i-1], i+1])
    return lst5
            
# we print out the what is returned from the function list_of_list_generator_modified           
print(list_of_list_generator_modified(3))
