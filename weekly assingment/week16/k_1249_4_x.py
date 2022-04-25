'''
T = int(input())
for t in range(1, T + 1):
    length = int(input())
    grid = []
    record = {}
    for i in range(length):
        grid.append(list(map(int,input())))
    
    def route(i,j,t):
        if not  (0<=i<length and 0<=j<length):
            return 
        if (i,j) not in record:
            record[(i,j)] = t+grid[i][j]
        else:
            record[(i,j)] = min(t+grid[i][j],record[(i,j)])
        
        #if d!="u" and visited.count(i+1,j) < 5: route(i+1,j,record[(i,j)],"d")
        #if d!="l" and visited.count(i,j+1) < 5: route(i,j+1,record[(i,j)],"r")
        route(i-1,j,record[(i,j)])
        route(i,j-1,record[(i,j)])
        
    route(length-1,length-1,0)
    print("#{} {}".format(t,record[(0,0)]))
  '''  
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(arr):
    queue = arr
    while queue:
        new = []
        while queue:
            [x,y] = queue.pop()
            for i in range(4):
                x2 = x + dx[i]
                y2 = y + dy[i]
                if 0 <= x2 < n and 0 <= y2 < n:
                    temp = ans[x][y] + graph[x2][y2]
                    if temp < ans[x2][y2]:
                        ans[x2][y2] = temp
                        new.append([x2,y2])
        queue = new
for t in range(int(input())):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    ans = [[10000 for _ in range(n)] for _ in range(n)]
    ans[0][0] = graph[0][0]
    bfs([[0,0]])
    print(f"#{t+1} {ans[n-1][n-1]}")
