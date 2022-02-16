# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        result = ListNode()
        pointer = result
        while head.next != None:
            pointer.next = ListNode(head.next.val,ListNode(head.val))
            head = head.next
            pointer = pointer.next.next
            
            if head.next == None: break
            else:
                head = head.next
                if head.next == None:
                    pointer.next = head
                    break

        return result.next
            
            
