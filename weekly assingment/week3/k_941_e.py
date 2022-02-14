class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 1 or arr[0] > arr[1]:
            return False
        point = arr[0]
        bent = False
        for i in range(1,len(arr)):
            if not bent:
                if point == arr[i]:
                    return False
                elif point < arr[i]:
                    point = arr[i]
                else:
                    point = arr[i]
                    bent = True
            else:
                if point > arr[i]:
                    point = arr[i]
                else:
                    return False
        if bent:
            return True
        else:
            return False