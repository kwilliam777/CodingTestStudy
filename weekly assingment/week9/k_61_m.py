# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None
        if head.next == None: return head
        
        count = 1
        pointer = head
        nodes=[head]
        while pointer:
            if pointer.next == None:
                pointer.next=head
                break
            pointer=pointer.next
            nodes.append(pointer)
            count+=1
            
        k = k%count
        if k != 0:
            nodes[count-k-1].next = None
            return nodes[count-k]
        else:
            nodes[-1].next = None
            return nodes[0]
        
            
