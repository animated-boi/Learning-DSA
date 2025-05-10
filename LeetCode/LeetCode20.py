'''
LeetCodee 20 : VALID PARENTHETISIS
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if s[i] in ['(', '[', '{' ]:
                stk.append(s[i])
            else:
                if stk:
                    chr = stk.pop()
                    if (chr == '(' and s[i] !=')' ) or (chr == '[' and s[i] !=']' ) or (chr == '{' and s[i] !='}'):
                        return False
                else:
                    return False
        if not stk:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isValid(''))