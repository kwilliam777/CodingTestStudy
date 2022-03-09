# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        if head.next == None: return head

        vals = []
        removed = []
        while head != None:
            val = head.val
            if val not in vals: 
                if val not in removed:    
                    vals.append(val)
            else:
                vals.remove(val)
                removed.append(val)
            head = head.next
        
        if len(vals) == 0: return None
        
        result = ListNode(vals[0])
        pointer = result
        for i in range(1,len(vals)):
            pointer.next = ListNode(vals[i])
            pointer = pointer.next
        
        return result
    
    
    
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         sentinel = ListNode(0, head)
#         pred = sentinel
        
#         while head:
#             if head.next and head.val == head.next.val:
#                 while head.next and head.val == head.next.val:
#                     head = head.next
#                 pred.next = head.next 
#             else:
#                 pred = pred.next 
#             head = head.next
            
#         return sentinel.next
