class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rec = []
        while head:
            rec.append(head.val)
            head=head.next
        return rec==rec[::-1]
