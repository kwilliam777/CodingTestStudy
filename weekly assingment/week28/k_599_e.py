class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        both = [(list1.index(i)+list2.index(i),i) for i in set(list1+list2) if i in list1 and i in list2]
        both.sort(key = lambda x:x[0])
        return [i[1] for i in both if i[0]==both[0][0]]
