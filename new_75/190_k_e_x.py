# class Solution:
#     def reverseBits(self, n: int) -> int:

        
        
# class Solution:
# 	def reverseBits(self, n: int) -> int:
# 		binary_number = bin(n)[2:]
# 		binary_number = '0'*(32-len(binary_number))+binary_number
# 		reverse_binary_number = binary_number[::-1]
# 		return int(reverse_binary_number, 2)
    
    
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for _ in range(32):
#             res = (res<<1) + (n&1)
#             n>>=1
#         return res
