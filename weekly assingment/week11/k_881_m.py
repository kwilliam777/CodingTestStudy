class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        front = 0
        back = len(people)-1
        
        while front != back:
            if people[front]+people[back] > limit:
                back -= 1
                count += 1
            else:
                if back-front == 1:
                    front += 1
                else:
                    front += 1
                    back -= 1
                    count += 1
            
        return count+1
    
    
    
# class Solution(object):
#     def numRescueBoats(self, people, limit):
#         people.sort()
#         i, j = 0, len(people) - 1
#         ans = 0
#         while i <= j:
#             ans += 1
#             if people[i] + people[j] <= limit:
#                 i += 1
#             j -= 1
#         return ans
