from collections import Counter 
class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}
        self.recent = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        
    def pop(self) -> int:
        self.count = Counter(self.stack)
        self.maxn = max(self.count[key] for key in self.count)
        self.recent = [i for i in self.count if self.count[i] == self.maxn]

                    
        for i in range(len(self.stack)-1,-1,-1):
            if len(self.recent) == len(self.stack):
                return self.stack.pop(-1)
            elif self.stack[i] in self.recent:
                return self.stack.pop(i)

            
# class FreqStack:

#     def __init__(self):
#         self.stks = []
#         self.freq = defaultdict(int)
        
#     def push(self, val: int) -> None:
#         self.freq[val] += 1
#         if self.freq[val] > len(self.stks):
#             self.stks.append([val])
#         else:
#             self.stks[self.freq[val]-1].append(val)
            
#     def pop(self) -> int:
#         while not self.stks[-1]:
#             self.stks.pop()
#         val = self.stks[-1].pop()
#         self.freq[val] -= 1
#         return val
