'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#UNDERSTAND (U)
#presented with an array data structure with a list of intergers
#are there constraints where only positive intergers or numbers less than 0 can be added to the list?

#input
#list of intergers that contains duplicates, expect for one interger

#output
#if there is a duplicate number in the list, then just return the list or return None
#if the interger is not a duplicate, then return that single interger

#PLAN(P)
#need to loop through the list of intergers to find the one that does not contain the duplicate
#conditional statements- if there is duplicate interger that return the list
    #else if the interger is a duplicate
    #return that interger found in the array index

#EXECUTE (E)
#how to check if interger is a duplicate or not?
#create an empty array that will hold the single intergers
#use append and remove method for array

def single_number(arr):
    # Your code here

    #create an array that will hold the single interger
    single = []

    #loop through every element in the arr
    for i in arr:
        #if element doesn't exist in single array than append that item to single array
        if i not in single:
            single.append(i)
        else:
        #if the i element has already been added to the single array then remove it.  
        #duplicates are then removed
            single.remove(i)
    #return the first item from the single array where the single interger should remain
    return single[0]

    # #2nd solution also works for Day 2

    #If we add each number once and multiply the sum by 2, 
    # we will get twice sum of each element of the array. 
    # Then we will subtract the sum of the whole array from the twice_sum 
    # and get the required number (which appears once in the array).#

    #set method creates an array with unique elements. Doesn't allow duplicates
    #    2* sum(arr no duplicates) -sum(array)    
    # return 2 * sum(set(arr))- sum(arr)
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")