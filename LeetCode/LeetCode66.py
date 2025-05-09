# Approach 1 Thinking
# nums = [9]

# word = "".join(str(num) for num in nums)
# word = int(word) + 1

# print(list(str(word)))

#Approach 1
from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         word = "".join(str(num) for num in digits)
#         word = int(word) + 1

#         return(list(int(i) for i in list(str(word))))
    


#Approach 2 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            if carry:
                if digits[i] != 9:
                    digits[i] += 1
                    carry = 0
                else:
                    digits[i] = 0
        
        if carry:        
            digits = [1] + digits

        return digits

sol = Solution()
print(sol.plusOne([ 9, 9, 9]))