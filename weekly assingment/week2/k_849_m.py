class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxdist = [0]
        tempdist = 0
        
        for seat in seats:
            if seat == 1:
                if max(maxdist) < tempdist:
                    maxdist.append(tempdist)
                maxdist.append(0)
                tempdist = 0
            elif seat == 0:
                tempdist += 1
        maxdist.append(tempdist)
        for i in range(len(maxdist)):
            if 1<i<len(maxdist)-1:
                if maxdist[i]%2 == 0:
                    maxdist[i] = int(maxdist[i]/2)
                else:
                    maxdist[i] = int(maxdist[i]/2)+1
        print(maxdist)
        return max(maxdist)