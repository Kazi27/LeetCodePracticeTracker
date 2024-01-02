// Problem:
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Example 1:
// Input: nums = [1,2,3,1]
// Output: true

// Example 2:
// Input: nums = [1,2,3,4]
// Output: false

// Example 3:
// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

// Solution:
#include <vector>
class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end()); //first sort the vector, once sorted duplicates will be side by side each other
        for (int i = 0; i < nums.size() - 1; i++) //iterate through, it's size - 1 because you don't want to get an error for trying to find an index that not there so < 
        {
            if (nums[i] == nums[i+1]) //if the current element at the index matches that next to it, duplicate so true
            {
                return true;
            }
        }

        return false; //if ur here it means you checked it all and there are no duplicates
    }
};