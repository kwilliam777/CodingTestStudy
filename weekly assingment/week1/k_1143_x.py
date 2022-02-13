class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) == 1:
            if text2 in text1:
                return 1
        index = 0
        count = 0
        counts = [0]
        for i in text2:
            if i in text1:
                temp2 = text2[text2.index(i)+1:]
                for j in temp2:
                    temp1 = text1[text1.index(i)+1:]
                    if j in temp1:
                        tempIndex = temp1.index(j)
                        print(temp1,temp2)
                        if tempIndex < index:
                            
                            counts.append(count+1)
                            index = 0
                            count = 0
                            break
                        elif index <= tempIndex:
                            index = tempIndex
                            count += 1
                        if temp2.index(j) == len(temp2) - 1:    
                            counts.append(count+1)
                            count = 0
                            index = 0
                    else:
                        counts.append(count+1)
        if len(counts) == 1 and text1[-1] == text2[-1]:
            counts.append(1)
        return max(counts)
