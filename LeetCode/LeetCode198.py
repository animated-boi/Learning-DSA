'''
Leet Code 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

#wrong Solution - USE DP
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(0, len(nums), 2):
            rob1 += nums[i]
        
        for j in range(1, len(nums), 2):
            rob2 += nums[j]
        print(rob1, rob2)
        if rob1 > rob2:
            return rob1
        else: return rob2



sol = Solution()
print(sol.rob([1,2,3,1]))