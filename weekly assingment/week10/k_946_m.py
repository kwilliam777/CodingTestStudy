class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        bef, aft = [],[]
        for i in popped:
            if i in pushed:
                while i in pushed:
                    bef.append(pushed.pop(0))
                aft.append(bef.pop())    
            elif i in bef:
                while i in bef:
                    aft.append(bef.pop())

        return False if popped != aft else True           
        
# 내가 더 빠름 ㅋ
# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         stack=[]
#         i=0
#         for num in pushed:
#             stack.append(num) #we are pushing the number to the stack
#             while  len(stack) >0 and stack[len(stack)-1] == popped[i] :
#                 #if the last element of the stack is equal to the popped element
#                 stack.pop()
#                 i+=1 #we are incrementing i
#         return True if len(stack) ==0 else False
