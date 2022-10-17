class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(set(sentence)) == 26 else False
