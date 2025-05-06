from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        Left =  self.binary_search(nums, target, False)
        Right =  self.binary_search(nums, target , True)
    
        return [Left, Right]

    def binary_search(self, nums, target, left_index = False):
            low, high = 0, len(nums) - 1
            i = -1
            while low <=  high: 
                mid = (low + high) // 2
                if nums[mid] == target:
                    i = mid
                    if left_index:
                        low = mid + 1
                    else:
                        high = high - 1 
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
            return i