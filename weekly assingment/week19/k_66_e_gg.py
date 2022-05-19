class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9: digits[-1]+=1
        else:
            for i in range(len(digits)-1,-1,-1):
                if i == 0:
                    if digits[i]==9:
                        digits[i]=0
                        digits.insert(0,1)
                    else:
                        digits[i]+=1
                elif digits[i] == 9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    break
                    
        return digits
