class KthLargest:
    ind = 0
    arr = []
    def __init__(self, k: int, nums: List[int]):
        self.ind = k-1
        self.arr = nums
        
    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort(reverse = True)
        return self.arr[self.ind]
