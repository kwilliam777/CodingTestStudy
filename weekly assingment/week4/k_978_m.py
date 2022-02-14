class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        elif len(arr) == 2:
            if arr[0] != arr[1]: return 2
            else: return 1
        
        maxlen, temp = 0,1
        check = arr[0] < arr[1]
        
        for i in range(1, len(arr)):
            if check:
                if arr[i-1] < arr[i]: temp += 1
                else:
                    check = not check 
                    if arr[i-1] == arr[i]: temp = 1
                    else: temp = 2
            else:
                if arr[i-1] > arr[i]: temp += 1
                else:
                    check = not check
                    if arr[i-1] == arr[i]: temp = 1
                    else: temp = 2
                    
            if maxlen < temp: maxlen = temp
            check = not check
            
        return maxlen