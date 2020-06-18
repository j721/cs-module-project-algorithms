'''
Input: an integer
Returns: an integer
'''
#
#  Implement a function eating_cookies that counts the number of possible 
# ways Cookie Monster can eat all of the cookies in the jar.

# For example, for a jar of cookies with n = 3 (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

# He can eat 1 cookie at a time 3 times
# He can eat 1 cookie, then 2 cookies
# He can eat 2 cookies, then 1 cookie
# He can eat 3 cookies all at once.
# Thus, eating_cookies(3) should return an answer of 4.#


#U
#need to store this data into memory to keep track of how many times the person is eating the cookie, like using cache?
#need to pass in cache or memory as a parameter and initialize to None

#n stands for number of cookies

#look up permutations and recursion
#as well as cache and memoization
#used ring buffer from sprint as reference as well

# P

# E
# R#

#Less efficient method
# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)




#n stands for input size- number of cookies in the jar
#pass in cache (memory storage holder) as parameter and default to none
#cache helps to make run time faster. data structure that stores redundant data
#cache is a dictionary where keys is the n, value is the answer

def eating_cookies(n, cache = None):
    # Your code here

    #if cache array is empty then initialize it
    if cache == None:
        cache = [0] * (n + 1) #(n+1) refering to the input size incrementing/increasing by 1. 
        

    #if input n is less than or equal to 1 than cache storage index will still be at 1
    #basically there is just one way to eat the cookie 
    # and there is one way where he can not eat the cookie
    if n <= 1:
        cache[n] = 1

    #if input of cookies is 2, then cache storage index will be at 2
    #there are 2 ways in which he eat the cookie
    elif n ==2:
        cache[n] = 2

    #edge case if the index of cache[n] is at 0 
    #ate all of the cookies at once (eating all 3 cookies)
    elif cache[n] == 0:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    #return number of ways to eat cookies
    return cache[n]

  

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
