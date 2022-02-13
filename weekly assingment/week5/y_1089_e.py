class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        checker=0
        for index in range(len(arr)) :
            if arr[index] == 0 and checker==0 :
                for i in range(len(arr)-1,index,-1) :
                    arr[i]=arr[i-1]
                checker=1
            else :
                checker=0
            
        return arr
             
