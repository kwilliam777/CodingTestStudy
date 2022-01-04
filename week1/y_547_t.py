class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def find(parent_list, index) :
            if parent_list[index]==-1 :
                return index;
            return find(parent_list,parent_list[index])
        
        def union (parent_list, x, y) :
            x_set = find(parent_list,x)
            y_set = find(parent_list,y)
            if (x_set != y_set) :
                parent_list[x_set] = y_set
        
        
        parent_list = [-1] * len(isConnected)
        
        for i in range(len(isConnected)) :
            for j in range (len(isConnected)) :
                if isConnected[i][j]==1 and i != j :
                    union(parent_list,i,j)
        
        
        count =0
 
        
        for i in  parent_list :
            if i== -1 :
                count+=1
                
        return count
        