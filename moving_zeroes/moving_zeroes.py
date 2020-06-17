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

# E
# R
# #


def moving_zeroes(arr):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")