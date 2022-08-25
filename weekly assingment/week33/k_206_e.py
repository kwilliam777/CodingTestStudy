class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur,pre = head, None
        while cur: cur.next,pre,cur = pre,cur,cur.next
        return pre
