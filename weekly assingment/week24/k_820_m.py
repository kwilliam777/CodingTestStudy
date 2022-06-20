# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:        
#         words = list(set(words))
#         words.sort(key = lambda x:len(x),reverse = True)
#         encode = [words.pop(0)]
        
#         for word in words:
#             overlap = False
#             for en in encode:
#                 if en.endswith(word):
#                     overlap = True
#                     break
#             if not overlap:
#                 encode.append(word)
#         return len(("#").join(encode))+1
    
    
class Solution:
    def minimumLengthEncoding(self, W: List[str]) -> int:
        wset = set(W)
        for word in W:
            if word in wset:
                for i in range(1,len(word)):
                    wset.discard(word[i:])
        return len("#".join(list(wset))) + 1
    
# class Solution:
#     def minimumLengthEncoding(self, W: List[str]) -> int:
#         trie, ans = defaultdict(), 1
#         for word in W:
#             curr, newWord = trie, False
#             for i in range(len(word)-1,-1,-1):
#                 char = word[i]
#                 if not curr and not newWord: ans -= len(word) - i
#                 if char not in curr:
#                     newWord = True
#                     curr[char] = defaultdict()
#                 curr = curr[char]
#             if newWord: ans += len(word) + 1
#         return ans
