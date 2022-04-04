# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        save = []
        pointer = head
        pre = ListNode(0,head)
        
        while pointer!=None:
            if pointer.val not in save:
                save.append(pointer.val)
                pre.next = pointer
                pre = pre.next
            pointer = pointer.next
        pre.next = None
            

        return head
    
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         cur=head
#         while cur:
#             if cur.next and cur.next.val==cur.val:
#                 cur.next=cur.next.next
#             else:
#                 cur=cur.next
#         return head
