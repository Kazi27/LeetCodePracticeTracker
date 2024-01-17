
# Problem:
# Reverse bits of a given 32 bits unsigned integer.
 
# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

# Solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 #32 bit length of 0
        for i in range(32): #32 bits
            x = (n >> i) #bit shift right n by i, target bit wil be in 1 spot
            bit = x & 1 #this variable will have the desired bit
            y = bit << (31 - i) #bitshift it to the left, actual reversal here
            #first iteration 31 - 1 = 30 so it'll be bit shifted to the left by 30
            result = result | y #the or operation, store reversed in result
        return result #return result
    
# Complexities:
# The time complexity is O(1) because we are guaranteed the bits are just 32 binary digits
# The memory complexity is also O(1) because we are just having variables