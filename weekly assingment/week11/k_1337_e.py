class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # ans = [(i,sum(val)) for i,val in enumerate(mat)]
        # for i,val in enumerate(mat):
        #     ans.append((i,sum(val)))
        # ans = sorted(ans,key=lambda x:x[1])
        return [i[0] for i in sorted([(i,sum(val)) for i,val in enumerate(mat)],key=lambda x:x[1])[:k]]
    
        # mat = [sum(i) for i in mat]
        # ans = []
        # temp = sorted(mat)
        # for i in temp:
        #     if i in mat:
        #         ind = mat.index(i)
        #         ans.append(ind)
        #         mat[ind] = -1
        #         if len(ans) == k:
        #             return ans
        
        
        
    
