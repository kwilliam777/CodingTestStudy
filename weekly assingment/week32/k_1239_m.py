class Solution:
    def maxLength(self, arr: List[str]) -> int:
        tot = len(arr)
        for i in range(tot):
            for j in range(i,len(arr)):
                temp = arr[i]+arr[j]
                if len(temp) == len(set(temp)):
                    arr.append(temp)
        res = [len(i) for i in arr if len(i) == len(set(i))]
        return max(res) if len(res) > 0 else 0
