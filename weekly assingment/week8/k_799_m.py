class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured > 6000:
            return 1.00000
        elif poured == 1:
            if query_row == 0 and query_glass == 0:
                return 1.00000
            else:
                return 0.00000
            
            
        poured -= 1  
        for i in range(1,query_row+1):
            if poured/(i*2) >= 1:
                if query_row <= i:
                    print(1,poured,i)
                    return 1.00000
                else:
                    poured -= (i+1)
            else:
                if query_row >= i:
                    if query_glass == 0 or query_glass == i:
                        print(2,poured,i)
                        return poured/(i*2)
                    else:
                        print(3,poured,i)
                        return poured/i
                else:
                    return 0.00000
                
                
                
# class Solution(object):
#     def champagneTower(self, poured, query_row, query_glass):
#         A = [[0] * k for k in range(1, 102)]
#         A[0][0] = poured
#         for r in range(query_row + 1):
#             for c in range(r+1):
#                 q = (A[r][c] - 1.0) / 2.0
#                 if q > 0:
#                     A[r+1][c] += q
#                     A[r+1][c+1] += q

#         return min(1, A[query_row][query_glass])
