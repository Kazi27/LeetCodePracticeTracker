
# Problem:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Solution:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()  #sort nums so once sorted, duplicates will be next to each other
        for i in range(len(nums) - 1):  #ierate through, len(nums) - 1 to avoid index out of range
            if nums[i] == nums[i + 1]:  #if current element at the index matches the next one, it's a duplicate
                return True

        return False  # If you reach here, it means you checked it all, and there are no duplicates

# Time Complexity:
# The time complexity for sorting is O(n log n), and then the loop runs n times. Overall, it takes O(n log n)
