# class Solution:
#     def longestPalindrome(self, s: str) -> str:

#         if len(s) < 2: return s
#         maxl = str()
        
#         for i in range(len(s)):
#             shorter = i if i <= len(s)-i else len(s)-i
#             for j in range(len(maxl)//2,shorter*2+2):
#                 ind1 = i-j//2
#                 ind2 = i+j//2
#                 if j%2 == 0 and s[ind1+1:ind2+2] == s[ind1+1:ind2+2][::-1]:
                    
#                     maxl = maxl if len(maxl) > len(s[ind1+1:ind2+2]) else s[ind1+1:ind2+2]
#                 elif j%2 == 1 and s[ind1:ind2+2] == s[ind1:ind2+2][::-1]:
                    
#                     maxl = maxl if len(maxl) > len(s[ind1:ind2+2]) else s[ind1:ind2+2]
#                 print(i,j,ind1,ind2,s[ind1:ind2+2])
#         return maxl

    
    
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, max_len, ans = len(s), 0, ''
        def expand_around_center(l, r):
            if r < n and s[l] != s[r]:
                return '' # Index out of range or elements unequal(for even sized palindromes) thus return empty string
            while l >= 0 and r < n and s[l] == s[r]: # Till the s[l], s[r] elements are in range and same, the palindrome continues to grow
                l, r = l - 1, r + 1
            return s[l + 1:r] # Return the palindrome formed
        for i in range(n):
            a, b = expand_around_center(i, i), expand_around_center(i, i + 1) # (i,i) for odd and (i,i+1) for even sized palindromes
            main = a if len(a) > len(b) else b # Check which one of a, b is larger
            if len(main) > max_len: # Check if palindrome with i as center is larger than previous entries then update if necessary
                max_len, ans = len(main), main
        return ans
