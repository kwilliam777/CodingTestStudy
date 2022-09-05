class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None: return []
        childs = [[root]]
        rec = []
        while childs:
            vals = []
            nextchild = []
            cur = childs.pop(0)
            for child in cur:
                if child != None:
                    vals.append(child.val)
                    nextchild+=child.children
                
            if len(nextchild)>0: childs.append(nextchild)
            rec.append(vals)
            
        return rec
