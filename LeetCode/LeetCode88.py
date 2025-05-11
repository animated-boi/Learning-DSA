'''
Leet Code 88 : MERGED TWO SORTED ARRAYS

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

'''
from typing import List
#Approach 1 - Extra Array    #Time = O(m+n) #Space = O(m+n)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums = [0]* (m+n)
#         i, j, k = 0, 0, 0
#         while i < m and j < n:
#             if nums1[i] <= nums2[j]:
#                 nums[k] = nums1[i]
#                 i += 1
#             else:
#                 nums[k] = nums2[j]
#                 j += 1
#             k += 1
        
#         while i < m :
#             nums[k] = nums1[i]
#             i, k = i + 1, k + 1
        
#         while j < n :
#                 nums[k] = nums2[j]
#                 j, k = j + 1, k + 1
               
#         return nums


#Approach 2 - In-place   #Time = O(m+n) #Space = O(1)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         # """
        # i = m - 1
        # j = n - 1
        # k = m + n -1
        
        # while i >= 0 and j >= 0:
        #     if nums1[i] <= nums2[j]:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     else:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     k -= 1
        
        # while j >= 0 :
        #         nums1[k] = nums2[j]
        #         j, k = j - 1, k - 1
        # while i >= 0 :
        #         nums1[k] = nums1[i]
        #         i, k = i - 1, k - 1

        # return nums1

#OPTIMISED APPROACH 2 - 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        # """
        i = m - 1
        j = n - 1
        k = m + n -1

        while j>= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1 
            k = k - 1
            
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
                


