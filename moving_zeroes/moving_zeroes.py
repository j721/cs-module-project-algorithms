'''
Input: a List of integers
Returns: a List of integers
'''

#Understand-U
# takes an array of intergers
# want to move non-zero interger to the left
#can include negative or positive intergers
#order in which non-zero intergers are moved to the left doesn't matter (doesn't have to be sorted)
# zero is moved all the way to the right of the array


# Plan- P
#need to iterate/loop over array length -1 to determine if interger is equal to zero or not

#if zero does exist in the array then
#elif the interger is zero then move to the right of the array (meaning the end of the array)
#zero will be at the very end, last index of the array
#else the interger is a non-zero interger then we will increment it to move towards the left
# towards the beginning of the array
#else if zero does not exist in array 
#then just return the array back

# Execute (E)
#need to initialize count to 0
#use for loop to iterate through array
# if index at array arr[i] !== 0
  #  return arr

# Reflect
#referenced Data Structures Project- doubly_linked list file. move_to_end function for 2nd method
# #


def moving_zeroes(arr):
    # Your code here

    #initialize count to zero
    # count = 0
    # #loop through array
    # for i in range(len(arr)):
    #     #if we encounter a non-zero interger in the array
    #     if arr[i] !=0:
    #         #increment by +1 into the counter
    #         count +=1
    #         #array order will now be the array at index i, the zero will be at the end [:i], the non-zero intergers will be on the left [i+1] referring to the counter
    #         arr = [arr[i]] + arr [:i] + arr[i+1:]
    # return(arr)





    #2nd method
    #Just remove the 0 from the array, and add it back to the end of the array
    #use Remove method to remove the 0 from array
    # use append method to add the 0 to the end of the array
    #still have to loop through array 


    #initialize count    
    count = arr.count(0)
    #loop through array 
    for i in range(0, count):
        arr.remove(0) #remove method to remove 0
        arr.append(0) #append method adds 0 to the end of the array     #similar to insertion method
    return arr

        


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")