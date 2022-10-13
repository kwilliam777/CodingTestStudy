class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = None if node.next.next == None else node.next.next   
