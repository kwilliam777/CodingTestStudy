class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(list(s1))
        result = False
        for i in range(len(s1),len(s2)+1):
            temp = sorted(s2[i-len(s1):i])
            if temp == s:
                return True
        return False

# class Solution:
#     def checkInclusion(self, s1, s2):
#         A = [ord(x) - ord('a') for x in s1]
#         B = [ord(x) - ord('a') for x in s2]
#         if len(A) > len(B): return False
    
#         target = [0] * 26
#         for i in range(len(A)):
#             target[A[i]] -= 1
#             target[B[i]] += 1
        
#         num_to_correct = sum([i != 0 for i in target])
#         if num_to_correct == 0: return True
            
#         for i in range(len(A), len(B)):
#             new_s = B[i]
#             target[new_s] += 1
#             if target[new_s] == 0: num_to_correct -= 1
#             if target[new_s] == 1: num_to_correct += 1
                
#             old_s = B[i - len(A)]
#             target[old_s] -= 1
#             if target[old_s] == -1: num_to_correct += 1
#             if target[old_s] == 0: num_to_correct -= 1
                                
#             if num_to_correct == 0: return True  
                    
#         return False
