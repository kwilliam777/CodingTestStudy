class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        result = [letter.isupper() for letter in word]
        count = Counter(result)
        if count[True] == len(word) or (count[True] == 1 and result[0] == True) or count[True] == 0:
            return True
        return False