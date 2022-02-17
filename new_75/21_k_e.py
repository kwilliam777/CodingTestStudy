# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: 
        done = False
        l1,l2 = [],[]
        
        while not done:
            if list1 == None and list2 == None: break
            elif list1 == None:
                l2.append(list2.val)
                if list2.next == None: break
                list2 = list2.next
            elif list2 == None:
                l1.append(list1.val)
                if list1.next == None: break
                list1 = list1.next
            else:
                l1.append(list1.val)
                l2.append(list2.val)
                if list1.next == None: list1 = None
                else: list1 = list1.next
                    
                if list2.next == None: list2 = None
                else: list2 = list2.next
                
        result = l1+l2
        result.sort()
        
        if len(result) == 0: return None
        
        ans = ListNode()
        pointer = ans
        for i in result:
            ans.next = ListNode(i)
            ans = ans.next
        
        return pointer.next
    
    
