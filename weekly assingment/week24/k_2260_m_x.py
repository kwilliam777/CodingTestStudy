class Solution:
    # def minimumCardPickup(self, cards: List[int]) -> int:
#         left = 0
#         right = 1
#         mini = len(cards)+1
        
#         while left < len(cards)-1:
#             # print(left,right,set(cards[left:right]),cards[left:right])
#             if len(set(cards[left:right]))==len(cards[left:right]):
#                 if right == len(cards):
#                     break
#                 right+=1
#             else:
#                 if mini > len(cards[left:right]):
#                     mini = len(cards[left:right])
#                 left+=1
#         return -1 if mini == len(cards)+1 else mini
    
    
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = math.inf
        n = len(cards)
        pos = defaultdict(lambda: -1)
        for i in range(n):
            if pos[cards[i]] != -1:
                ans = min(i - pos[cards[i]] + 1, ans)
            pos[cards[i]] = i
        return ans if ans != math.inf else -1
