class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # temp = list(s)
        # for i in range(len(spaces)):
        #     temp.insert(spaces[i]+i," ")
        # return "".join(temp)
        # for i in range(len(spaces)):
        #     s = s[:spaces[i]+i] + " " + s[spaces[i]+i:]
        # return s
        spaces.insert(0,0)
        return " ".join([s[i:j] for i, j in zip(spaces, spaces[1:]+[None])])