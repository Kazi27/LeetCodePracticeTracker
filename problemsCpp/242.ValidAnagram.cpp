
// Problem:
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:
// Input: s = "rat", t = "car"
// Output: false

// Solution:
#include <string>
class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.size() == t.size()) //base condition, all anagrams will have same length, if not then they're not anagrams
        {
            std::sort(s.begin(), s.end());
            std::sort(t.begin(), t.end()); //sort both strings, all anagrams sorted will result in equivalent strings
            
            if (s == t)
            {
                return true; //strings match
            }
        }
        return false; //if ur here, s.size != t.size or sorted strings are not the same so not anagrams
    }
};

// Time Complexity:
// The time complexity for std::sort is O(n log n) and then you're sorting both strings so O(n log n) twice which generalizes to O(n log n)