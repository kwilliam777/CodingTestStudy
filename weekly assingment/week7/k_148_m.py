# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head != None:
            vals.append(head.val)
            head = head.next
        
        result = ListNode()
        pointer = result
        for v in sorted(vals):
            pointer.next = ListNode(v)
            pointer = pointer.next
            
        return result.next
