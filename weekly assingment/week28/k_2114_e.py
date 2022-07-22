class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([i.count(" ")+1 for i in sentences])
