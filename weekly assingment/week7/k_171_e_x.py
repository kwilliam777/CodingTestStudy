# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         count = 0 # 65 90
#         for i in range(len(columnTitle)):
#             if i == len(columnTitle)-1:
#                 count += ord(columnTitle[i])-64
#             else:
#                 count += 26**(len(columnTitle)-i)#*(ord(columnTitle[i])-64)
#         return count

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in columnTitle:
            ans = ans * 26 + ord(i) - ord('A') + 1
        return ans
