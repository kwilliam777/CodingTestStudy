class Solution:
    def validPalindrome(self, s: str) -> bool:
        temp = list(s)
        # print(temp, temp[::-1])
        if temp == temp[::-1]: 
            print("t")
            return True
        
        f = 0
        b = len(s)-1
        count = 0
        
        while b-f>0:
            if s[f]!=s[b]:
                if count == 1: return False
                if s[f+1]==s[b] and s[f+2]==s[b-1]:
                    f+=1
                    count+=1
                elif s[f]==s[b-1] and s[f+1]==s[b-2]:
                    b-=1
                    count+=1
                else:
                    return False
            f+=1
            b-=1
            # print(s[f],s[b],count)
        return True
    

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def check_palindrome(s, i, j):
#             while i < j:
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
            
#             return True

#         i = 0
#         j = len(s) - 1
#         while i < j:
#             # Found a mismatched pair - try both deletions
#             if s[i] != s[j]:
#                 return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
#             i += 1
#             j -= 1
        
#         return True
    
# class Solution(object):
#     def validPalindrome(self, s):
#         h, t = 0, len(s) - 1  # head and tail
#         while h < t:
#             if s[h] != s[t]:  # delete s[h] or s[t] and validate palindrome finally
#                  return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
#             h, t = h + 1, t - 1
#         return True
