#LeetCode 28. Find the Index of first occurence of the String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                elif j == len(needle) - 1:
                    return i
        
        return -1

#Approach 2 : FAANG Interview : Knuth-Morris-Pratt (KMP) algorithm : String Matching - 
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0

#         # Step 1: Build LPS array
#         def build_lps(pattern):
#             lps = [0] * len(pattern)
#             length = 0  # length of the previous longest prefix suffix
#             i = 1

#             while i < len(pattern):
#                 if pattern[i] == pattern[length]:
#                     length += 1
#                     lps[i] = length
#                     i += 1
#                 else:
#                     if length != 0:
#                         length = lps[length - 1]
#                     else:
#                         lps[i] = 0
#                         i += 1
#             return lps

#         lps = build_lps(needle)

#         # Step 2: KMP search
#         i = j = 0  # i for haystack, j for needle
#         while i < len(haystack):
#             if haystack[i] == needle[j]:
#                 i += 1
#                 j += 1
#                 if j == len(needle):
#                     return i - j  # match found
#             else:
#                 if j != 0:
#                     j = lps[j - 1]
#                 else:
#                     i += 1

#         return -1

sol = Solution()
print(sol.strStr('sunanimshanimansh', 'animan'))



