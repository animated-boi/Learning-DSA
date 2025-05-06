# Approach 1 Thinking
# nums = [9]

# word = "".join(str(num) for num in nums)
# word = int(word) + 1

# print(list(str(word)))

#Approach One
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = "".join(str(num) for num in digits)
        word = int(word) + 1

        return(list(int(i) for i in list(str(word))))