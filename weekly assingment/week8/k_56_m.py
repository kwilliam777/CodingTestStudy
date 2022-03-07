class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return None
        intervals = sorted(intervals , key=lambda x:x[0])
        intervals.append([float('inf'),float('inf')])
        
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in intervals:
            if i[0] <= end:
                if i[1] > end:
                    end = i[1]
            else:
                result.append([start, end])
                start, end = i
                
        return result
                
