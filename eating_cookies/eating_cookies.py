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
# P
# E
# R#

def eating_cookies(n):
    # Your code here

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
