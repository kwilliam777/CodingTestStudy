# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        
        result = ListNode()
        pointer = result
        nums = reversed(nums)
        for i in nums:
            pointer.next = ListNode(i)
            pointer = pointer.next
        return result.next
