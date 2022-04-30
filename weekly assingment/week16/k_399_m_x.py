class Solution:
    def calcEquation(self,equations, values, queries):
        G = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            G[x][y] = v
            G[y][x] = 1/v
        def bfs(src, dst):
            if not (src in G and dst in G): return -1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst: 
                    return v
                seen.add(x)
                for y in G[x]:
                    if y not in seen: 
                        q.append((y, v*G[x][y]))
            return -1.0
        return [bfs(s, d) for s, d in queries]
