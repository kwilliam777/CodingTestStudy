# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        store = []
        while pointer != None:
            store.append(pointer)
            pointer = pointer.next
        if n == 1:
            if len(store) == 1:
                return None
            else:
                store[-2].next = None  
        else:    
            if len(store) == n:
                head = head.next
            else:
                store[-(n+1)].next = store[-(n-1)]
        return head
    
    
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = fast = slow = ListNode(0, head)
        
#         for _ in range(n):
#             fast = fast.next
        
#         while fast and fast.next:
#             fast = fast.next
#             slow = slow.next
        
#         slow.next = slow.next.next
        
#         return dummy.next
