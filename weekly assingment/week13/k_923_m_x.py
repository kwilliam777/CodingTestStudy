# from collections import Counter 
# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         dic = Counter(arr)
#         keys = dic.keys()
#         count = 0
#         for i in range(len(arr)-2):
#             for j in range(i+1,len(arr)-1):
#                 count+=arr[j+1:].count(target-arr[i]-arr[j])
                
#         return count%(10**9+7)
    
    
# class Solution:
#     def threeSumMulti(self, A, T):
#         nmap, third, ans = [0 for _ in range(101)], ceil(T / 3) - 1, 0
#         for num in A: nmap[num] += 1
#         for k in range(min(T,100), third, -1):
#             rem = T - k
#             half = ceil(rem / 2) - 1
#             for j in range(min(rem, k), half, -1):
#                 i = rem - j
#                 x, y, z = nmap[i], nmap[j], nmap[k]
#                 if i == k: ans += x * (x-1) * (x-2) // 6
#                 elif i == j: ans += x * (x-1) // 2 * z
#                 elif j == k: ans += x * y * (y-1) // 2
#                 else: ans += x * y * z
#         return ans % 1000000007


class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return int(ans)
