# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None
        elif list1 == None: return list2
        elif list2 == None: return list1
        
        result = ListNode()
        pointer = result
        while not (list1 == None and list2 == None):
            if list1 == None:
                pointer.next = list2
                break
            elif list2 == None:
                pointer.next = list1
                break
            else:
                if list1.val < list2.val:
                    pointer.next = list1
                    list1 = list1.next
                else:
                    pointer.next = list2
                    list2 = list2.next
                pointer = pointer.next
            
        return result.next
    
#처음에 한거
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
#         result = []
#         done = False
#         l1 = []
#         l2 = []
#         while not done:
#             if list1 == None and list2 == None:
#                 break
#             elif list1 == None:
#                 l2.append(list2.val)
#                 if list2.next == None:
#                     break
#                 list2 = list2.next
#             elif list2 == None:
#                 l1.append(list1.val)
#                 if list1.next == None:
#                     break
#                 list1 = list1.next
#             else:
#                 l1.append(list1.val)
#                 l2.append(list2.val)
#                 if list1.next == None:
#                     list1 = None
#                 else:
#                     list1 = list1.next
#                 if list2.next == None:
#                     list2 = None
#                 else:
#                     list2 = list2.next
                
#         result = l1+l2
#         result.sort()
        
#         if len(result) == 0: return None
        
#         ans = ListNode()
#         pointer = ans
#         for i in result:
#             ans.next = ListNode(i)
#             ans = ans.next
        
        
#         return pointer.next
    
