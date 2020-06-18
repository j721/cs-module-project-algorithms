'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

#Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, 
# one element at a time.
#  You can only interact with the k amount numbers at a time in the window.
#  Return an array consisting of the maximum value of each window of elements.
# #

#U
#first array is list of intergers (nums)
#second array is the window that has a 'k' amount of elements its array
#third array returns the max value of each window of elements

#window moves from left to right (beginning to end) of array

# P
#possibly call recursion
#need to iterate over array, with window array set to k amount/limit
#another for loop over the array
    #need to calculate the max value
    #maybe think of as a node list?
# E
# R
# #
def sliding_window_max(nums, k):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
