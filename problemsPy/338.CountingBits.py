
# Problem:
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Solution:
class Solution:
    from typing import List
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1) #length is n + 1
        offset = 1 #most significant bit or highest power of 2 so far
        for i in range(1, n + 1): #runs upto n
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset] #forumla from drawing in the video, not sure how to explain it better
        return dp
    
# Complexities:
# The time complexity for this dynamic programming question in this solution is O(n) as the for loop runs n times
# The space complexity is also O(n) because the dp array will hold n elements