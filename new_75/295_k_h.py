# import statistics
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        # return statistics.median(self.arr)
        (self.arr).sort()
        l = len(self.arr)
        if l%2==0:
            return(self.arr[l//2-1] + self.arr[l//2])/2
        else:
            return(self.arr[l//2])
