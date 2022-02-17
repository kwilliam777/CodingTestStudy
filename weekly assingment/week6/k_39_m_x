class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []                                   # for adding all the answers
        def traverse(candid, arr,sm):                   # arr : an array that contains the accused combination; sm : is the sum of all elements of arr 
            if sm == target: self.ans.append(arr)       # If sum is equal to target then you know it, I know it, what to do
            if sm >= target: return                     # If sum is greater than target then no need to move further.
            for i in range(len(candid)):                # we will traverse each element from the array.
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])   #most important, splice the array including the current index, splicing in order to handle the duplicates.
        traverse(candidates,[], 0)
        return self.ans
     
    
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.calHelper([], 0, candidates, target, res)
        return res
        
    def calHelper(self, currentList, startIdx, candidates, target, res):
        # Once target == 0 means we found a vaild list
        if target == 0:
            res.append(currentList)
            return
        
        # Start from startIdx means we can use duplicate nums
        for i in range(startIdx, len(candidates)):
            num = candidates[i]
            if num <= target:
                self.calHelper(currentList + [num], i, candidates, target - num, res)
            # Since candidates are sorted, if we cant find a vaild num <= target we break
            else:
                break
