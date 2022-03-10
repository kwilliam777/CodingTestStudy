class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        elif newInterval[0] == newInterval[1]:
            if newInterval[0] in [i[1] for i in intervals] or newInterval[0] in [i[0] for i in intervals]:
                return intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        overlap = []        
        result = []
        for i in intervals:
            result.append(i)
            if newInterval[0]<=i[1]<newInterval[1] or newInterval[0]<i[0]<=newInterval[1] or (i[0]<=newInterval[0]<i[1] and i[0]<newInterval[1]<=i[1]):
                if i not in overlap:
                    overlap.append(i)
                    result.pop()
        if len(overlap) == 0: 
            intervals.append(newInterval)
            return sorted(intervals,key = lambda x:x[0])
        result.append([min(overlap[0][0],newInterval[0]),max(overlap[-1][1],newInterval[1])])
        return sorted(result, key=lambda x:x[0])
