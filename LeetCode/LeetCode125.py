'''
Leet Code 125: VALID PALINDROME

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''
# Approach 1 - Time : O(n) & Space : O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         stk=[]
#         for i in range(len(s)):
#             if ('A' <= s[i] <= 'Z') or ('a' <= s[i] <= 'z') or ('0' <= s[i] <= '9'):
#                 stk.append(s[i].lower())
        
#         l, r = 0, len(stk) - 1
#         while l <= r:
#             if stk[l] != stk[r]:
#                 return False
#             else:
#                 l, r = l + 1, r - 1
#         return True


# Approach 2 - Time : O(n) & Space : O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(chr):
            if ('a' <= chr <= 'z') or ('0' <= chr <= '9'):
                return True
            return False

        l, r = 0, len(s) - 1
        while l <= r:
            if  not isAlphaNum(s[l].lower()):
                l += 1
            elif not isAlphaNum(s[r].lower()):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l, r = l + 1, r - 1
        return True





sol = Solution()
print(sol.isPalindrome('An im"iNa!'))