# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None: return None
        save = []
        while head:
            save.append(head.val)
            head = head.next
        
        (save[k-1],save[-k]) = (save[-k],save[k-1])
        
        ans = ListNode(0)
        pointer = ans
        for i in save:
            pointer.next = ListNode(i)
            pointer = pointer.next
        
        return ans.next
    
    
    
    
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         first = last = head
#         for i in range(1, k):
#             first = first.next

#         null_checker = first 
#         while null_checker.next:
#             last = last.next
#             null_checker = null_checker.next
#         first.val, last.val = last.val, first.val
#         return head
