import numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]): return mat
        return numpy.reshape(mat,(r,c))

    
# class Solution(object):
#     def matrixReshape(self, mat, r, c):
#         elements = []
#         for row in mat:
#             elements += row
        
#         if len(elements) != r*c:
#             return mat
#         else:
#             new_mat = []
#             for row in range(r):
#                 mat_row = elements[:c]
#                 elements[:] = elements[c:]
#                 new_mat.append(mat_row)
#             return new_mat
