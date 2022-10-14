class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return head.next
        elif head.next.next == None:
            head.next = None
            return head
        save=slow=fast=pre=head
        while not (fast == None or fast.next == None):
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = slow.next
        return save 
