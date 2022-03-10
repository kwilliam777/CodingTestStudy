# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        pointer = result
        up = 0
        while l1 or l2:
            if l1 and l2:
                vals = l1.val + l2.val + up
                pointer.next = ListNode(vals%10)
                up = 1 if vals >= 10 else 0
                l1,l2 = l1.next, l2.next
            elif l2:
                vals = l2.val+up
                pointer.next = ListNode(vals%10)
                up = 1 if vals >= 10 else 0
                l2 = l2.next
            elif l1:
                vals = l1.val+up
                pointer.next = ListNode(vals%10)
                up = 1 if vals >= 10 else 0
                l1 = l1.next
            pointer = pointer.next
            
        if up == 1: pointer.next = ListNode(up)
            
        return result.next
    
    
# --------my old solution---------
#         num1 = str(l1.val)
#         num2 = str(l2.val)
#         list1 = l1
#         list2 = l2
#         while list1.next != None:
#             num1 = str(list1.next.val) + num1
#             list1 = list1.next
#         while list2.next != None:
#             num2 = str(list2.next.val) + num2
#             list2 = list2.next        
        
#         result = str(int(num1) + int(num2))
        
#         if len(result) == 1:
#             return ListNode(int(result))
#         elif len(result) == 2:
#             return ListNode(int(result[-1]), ListNode(int(result[-2])))
#         else:
#             total = ListNode(int(result[-1]), ListNode(int(result[-2])))
#             index = -3
#             temp = total
#             while index + len(result) != -1:
#                 if temp.next != None:
#                     temp = temp.next
#                 else:
#                     temp.next = ListNode(int(result[index]))
#                     index -= 1
#         return total
