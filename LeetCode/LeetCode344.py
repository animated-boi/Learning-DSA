#Approach 1
from typing import List
# Time =O(n) # Space = O(1) 
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i = len(s)-1
#         for j in range(0, ((len(s)-1)//2) + 1):
#             temp= s[j]                
#             s[j] = s[i]
#             s[i] = temp
#             i -= 1
        
#         return s

#Approach 1 Simplfied
# Time =O(n) # Space = O(1) 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[r], s[l] = s[l], s[r]
            l, r = l + 1, r - 1

        return s




#Approach 2 - Stack
# Time =O(n) # Space = O(n) 
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         stk =[]
#         for chr in s:
#             stk.append(chr)
    
#         i = 0
#         while stk:
#            s[i] = stk.pop()
#            i += 1
    
#         return s

#Appraoch 3 - Recurrsion
# Time =O(n) # Space = O(n) 
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         def reverse(l, r):
#             if l < r:
#                 s[l], s[r] = s[r], s[l]
#                 reverse(l+1, r-1)
#         reverse(0, len(s)-1)
#         return s


s = ["h","e","l","l", "o", "s", "z"]
sol = Solution()
print(sol.reverseString(s))



