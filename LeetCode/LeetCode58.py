#Approach 1
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         counter = 0
#         count = 0
#         for i in range(len(s)-1, -1, -1):
#             if s[i] == " ":
#                 count += 1
#             else: 
#                 break
#         for i in range(len(s)-1-count, -1, -1):
#             if s[i] != " ":
#                 counter += 1
#             else:
#                 return counter
        
#         return counter
    

#Approach 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_count = 0
        i =len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        while s[i] != ' ':
            word_count += 1
            i -= 1
    
        return word_count
    

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moonshines            ")) 