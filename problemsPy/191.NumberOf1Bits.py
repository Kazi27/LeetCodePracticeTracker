
# Problem:
# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

# Solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 #initialize count variable
        
        while n != 0: #at the end of the shifting it'll all be zeroes so you want to stop then
            x = n % 2 #x will be 1 if n is 1, 0 if n is 0
            if x == 1: #everytime x is one
                count = count + 1 #increment the count
            n = n >> 1 #bit shift n to the right by 1

        return count #return the count
    
# Complexities:
# For the time complexity, every input is a 32 bit integer so the while loop runs 32 times so time complexity is O(32) which is just O(1)
# For the space complexity, no data structures or anything we just bit shift which is very efficient for CPU anyways so space complexity is also O(1)