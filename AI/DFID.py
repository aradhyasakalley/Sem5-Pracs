from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DLS(self,src,target,maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        
        for i in self.graph[src]:
            if self.DLS(i,target,maxDepth-1):
                return True
        return False
    
    def IDDFS(self,src,target,maxDepth):
        for i in range(maxDepth+1):
            print(f"Iteration at depth {i}:")
            if self.DLS(src,target,i):
                return True
        return False

#   graph for dfid
#        0           -- depth 0
#      /   \
#     1     2       -- depth 1
#    / \    | \
#   3   4   5   6    -- depth 2

g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)


src = 0
target = 5
maxDepth = 2
if g.IDDFS(src,target,maxDepth):
    print(f'goal node {target} is reachable from src {src}')
else :
    print(f'goal node {target} is not reachable from src {src}')


