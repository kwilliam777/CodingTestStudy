class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        
        for i in range(1,len(searchWord)+1):
            find = searchWord[:i]
            res += [sorted([j for j in products if j.startswith(find)])[:3]]
                    
        return res
