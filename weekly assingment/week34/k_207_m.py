class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = [[] for _ in range(numCourses)]
        for i in prerequisites:
            preq[i[0]]+=[i[1]]
        pre = []
        took = set(i for i in range(len(preq)) if len(preq[i])==0)
        while pre != preq:
            pre = [i for i in preq]
            for i in [j for j in range(len(preq)) if len(preq[j])!=0]:
                if len(set(preq[i])&took)>0:
                    preq[i] = list(set(preq[i])-took)
                    if len(preq[i])==0:took.add(i)
                    break

            
        return True if len(sum(preq,[])) == 0 else False
