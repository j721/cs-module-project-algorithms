'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

#UNDERSTAND (U)
#presented with an array data structure with a list of intergers

#input
#list of intergers that contains duplicates, expect for one interger

#output
#if there is a duplicate number in the list, then just return the list or return None
#if the interger is not a duplicate, then return that single interger

#PLAN(P)
#need to loop through the list of intergers to find the one that does not contain the duplicate


def single_number(arr):
    # Your code here

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")