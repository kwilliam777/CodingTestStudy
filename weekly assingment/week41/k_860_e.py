class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        box = {5:0,10:0,20:0}
        for i in bills:
            if i==5: box[i]+=1
            elif i == 10:
                if box[5]==0: return False
                else:
                    box[i]+=1
                    box[5]-=1
            else:
                box[i]+=1
                if box[10]==0:
                    if box[5]<3: return False
                    else: box[5]-=3
                else:
                    if box[5]==0: return False
                    else:
                        box[10]-=1
                        box[5]-=1
        return True
