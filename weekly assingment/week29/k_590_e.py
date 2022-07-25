class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def deep(root):
            if root == None: return None    
            for i in root.children:
                deep(i)
            res.append(root.val)
        deep(root)
        return res
