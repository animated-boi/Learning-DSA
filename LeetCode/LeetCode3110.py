class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            print(ord(s[i]))
            val =  abs(ord(s[i+1]) - ord(s[i]))
            score += val
        return score
    

sol = Solution()
print(sol.scoreOfString("hello"))