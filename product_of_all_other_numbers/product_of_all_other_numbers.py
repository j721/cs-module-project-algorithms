'''
Input: a List of integers
Returns: a List of integers
'''
#Write a function that receives an array of integers 
# and returns an array consisting of the product of all numbers in the array 
# except the number at that index.
# #

#U
    #array of intergers should return the product of all the numbers in the array
    #excluding the element at that index
    #maybe remove that element at index, then doing the product for the rest of numbers in array
#P
    #if len(arr) <=1 then return -1 or just return the list
    #if array is greater than 1
        #then loop through items in the array
        #calculate product of numbers in array, but removing the specific number at that index arr[i]
        #
#E
#initialize product to hold empty array of products
#use nested for loops?
    #for loop to go over the interger array
    #for loop to go over the products array and check to make sure that index won't be included in product

    # to create product for when element a in array does not equal to element i from other for loop in original array
    #a!=i
    #then do *= to multiply the elements in the array to create a product

#R


def product_of_all_other_numbers(arr):
#     # Your code here

#     #create empty product array
    # product = []

    # #loop over the product array
    # for i in range(0, len(arr)):
    #     #initialize first product_item in the array as 1??
    #    #have the index element that was removed. Have its value now become 1
    #      #so that when calculating the rest of the products in the array, multiplying by 1 doesn't effect it
    #     product_item =1
    #     #loop through the other array that has the original intergers from the range of 0 to the length of the array
    #     for a in range(0, len(arr)):
    #         #at the index, the element a that was iterated over should not be equal to the index
    #         #if this condition is met then product_item will 
    #         if a!= i:
    #             product_item *= arr[a]
    #     product.append(product_item)

    # return product


    #2nd method
    #using the copy method- creates a shallow copy of the array
    #pop method- remove item and return that removed item at a given index
    #Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
    # This enumerate object can then be used directly in for loops
    #  or be converted into a list of tuples using list() method.


    # Syntax:

    # enumerate(iterable, start=0)

    # Parameters:
    # Iterable: any object that supports iteration
    # Start: the index value from which the counter is 
    #               to be started, by default it is 0 

    #created an empty array that will return the new product values
    new_arr = []

    #loops through the array
    #enumerate adds a counter to the iterable arr, starting at index of 0
    for i, num in enumerate(arr):
        #create copy of the original array of intergers
        copy = arr.copy()
        #pop method-removes the item at the given index and returns it
        #remove the item at that index
        copy.pop(i)
        #for the index element that was removed have its value now be 1, when calculating the product in the rest of the array
        product = 1
        #for each element x in the copy array
        for x in copy:
            #find the product of everything in the array excluding the index element, which now has a value of 1 which won't effect the product result/outcome
            product *=x
        #add the new product into the new_arr
        new_arr.append(product)
    return new_arr
                




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
