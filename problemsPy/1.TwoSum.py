
# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution:
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
    #def is to define a func in python
    #twoSum is func name
    #first parameter for any python func is always self, next param is nums with the type hint List[int] which means its a list of integers
    #third parameter is target which is is of type int
    #the thing after the -> is your return type in our case we return a list of integers
         
         prevMap = {} #initializes hashmap, will store every element before the last element of the pair, val : index
         
         for i, n in enumerate(nums): #first, enumerate gets the key and value from nums, then the key is given to i, value to n. Loop ends when nums ends
              
              diff = target - n #ur calculating the difference between the target and the value ur at in nums rn, if yes, thats ur solution
              
              if diff in prevMap: #if ur difference is in the hashmap, you found the solution already so return the indices
                    
                    return [prevMap[diff], i] #so prevMap[diff] goes searching into the map for the index whos val matches the diff val which we want. i is index ur currently at. U return both of these as per the problem
              
              prevMap[n] = i #if ur here, diff is not in hashmap so u add it, value of n goes into key at i

# Time Complexity:
# We are guaranteeing that by the time we reach the second element in the pair (which matches the diff) that our pair is complete because the diff plus the index ur currently at gives you the target
# So we just need O(n) time to accomplish this because we only iterate through the array once 