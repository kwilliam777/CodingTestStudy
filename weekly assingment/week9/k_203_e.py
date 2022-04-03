# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        vals = []
        while head!=None:
            if head.val != val:
                vals.append(head.val)
            head = head.next
                
        ans = ListNode()
        pointer = ans
        for i in vals:
            pointer.next = ListNode(i)
            pointer=pointer.next
        return ans.next
    
    
# class Solution:
#     def removeElements(self, head, val):
#         dummy_head = ListNode(-1)
#         dummy_head.next = head
        
#         current_node = dummy_head
#         while current_node.next != None:
#             if current_node.next.val == val:
#                 current_node.next = current_node.next.next
#             else:
#                 current_node = current_node.next
                
#         return dummy_head.next
