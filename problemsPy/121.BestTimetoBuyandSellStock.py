
# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Solution:
from typing import List
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        #u gotta buy before u sell, buy high sell low
        left = 0 #buy
        right = 1 #sell
        profit = 0 #initialize outside of forloop
        maxprofit = 0

        #while right < len(prices): 
        for x in range (1, len(prices)): #make sure u start @ 1, right starts at 1
        #just a regular for x in range(len(prices)) will not work
            if prices[left] < prices[right]: #when u buy low and sell high
                profit = prices[right] - prices[left] #ur profit
                if profit > maxprofit: #if ur new profit is more than prevprofit
                    maxprofit = profit
            
            else: #this is when ur buying high, selling low
                left = right #move left to right which is low
            
            right+=1 #move right till ur at the end
        
        return maxprofit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        #so two pointer problem
        left = 0 #buy
        right = 1 #sell
        maxprofit = 0 #initialize max profit

        while right < len(prices): #you want the right pointer to iterate thru all
            if prices[left] < prices[right]: #if buying less than what ur selling
                profit = prices[right] - prices[left] #calc the profit
                if profit > maxprofit: #if ur new profit is greater than previous
                    maxprofit = profit #this is ur new max profit
            else:
                left = right 
                #if ur here, ur selling lower than what ur buying for so move left
                #to that point so ur buying at this new low point rather than
                #selling at this point at aka left = right then right ++
            right += 1 #increase right by 1 till you reach end of the list
        
        return maxprofit            
    
# Complexities:
# Time complexity would be O(n) because we just use two pointers to iterate through the list, updating the left (buy) when it's at the lowest and right (sell) when it's at the highest
# Space complexity would be O(1) because we are just accessing arrays, no data struct or dynamic mem allocation