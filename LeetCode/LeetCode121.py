'''
LeetCode 121 : BEST TIME TPO BUY AND SELL STOCKS

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
from typing import List
#Approach 1 - Brute Force #Time : O(n^2) #Space : O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         p = 0
#         for i in range(len(prices) - 1):
#             # print(f"Loop for {prices[i]} , {i}")
#             max = 0
#             for j in range(i+1, len(prices)):
                
#                 diff = prices[j] - prices[i]
#                 # print(f"For {prices[j]} - {prices[i]} = {diff}")
#                 if diff > 0 and diff > max:
#                     max = diff
#             # print(f" Element for {i}, max is {max}")
#             if max > p:
#                 p = max
#         return p


#Approach 2 - Two Pointer #Time : O(n) #Space : O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy , sell = 0, 1
#         profit = 0
#         while sell < len(prices):
#             if prices[buy] < prices[sell]:
#                 profit = max(profit, (prices[sell] - prices[buy]))
#             else:
#                 buy = sell
#             sell += 1
                
#         return profit
    

#Approach 3 - DP #Time : O(n) #Space : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, (price - min_price))

        return max_profit

sol = Solution()
print(sol.maxProfit([7,6,4,3,1, 10]))