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
#possibly change the parameters when calling the range in the for loop
#need to iterate over array, with window array set to k amount/limit
#another for loop over the array
    #need to calculate the max value
    #take the length of array (nums) and subtract from that - k (limit for window) + 1
 
# E
#window should have a max of k(number amount)
#window min starts at 0
#create an array for that will hold the max value

#Use Python max() function
# The Python max() function returns the largest item in an iterable. 
# It can also be used to find the largest item between two or more parameters.

# R
# #
def sliding_window_max(nums, k):
    # Your code here

    #initialize window to have a min value at 0 and max value at k
    #create max_values array to be returned
    window_min = 0
    window_max = k
    max_values = []

    #traverse through nums array
    for i in nums:
        #have window in nums array be set within its limits of min and max
        window = nums[window_min: window_max]
        #once the window lands on a spot in the nums array calculate the max value of elements from that window
        #append the max value into the max_values array to be returned
        max_values.append(max(window))

        #if window_max is less than the length of the nums array
        #then increment the min and k to be able to calculate the max
        if window_max < len(nums):
            window_min +=1
            window_max +=1
        #else if the window_max exceeds/greater then the length of the nums array. Then there would be no window    
        else:
            break
    
    return max_values




    # max = [0] * (len(nums) - k +1)
    # window = []
    # for i in range (len(nums)- k +1):
    #     window = nums[i:i + k]
    #     max[i] = max(window)

    # return max




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
