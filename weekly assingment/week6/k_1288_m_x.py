# class Solution:
# 	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

# 		intervals=sorted(intervals)

# 		i=0
# 		while i<len(intervals)-1:

# 				a,b = intervals[i]
# 				p,q = intervals[i+1]

# 				if a <= p and q <= b:
# 					intervals.remove(intervals[i+1])
# 					i=i-1

# 				elif p <= a and b <= q:
# 					intervals.remove(intervals[i])
# 					i=i-1

# 				i=i+1
# 		return len(intervals)
    
    
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res, longest = len(intervals), 0
        srtd = sorted(intervals, key = lambda i: (i[0], -i[1]))
        print(srtd)    
        for _, end in srtd:
            if end <= longest:
                res -= 1
            else:
                longest = end
                
        return res
    
    
