visited = []
queue = []

def bfs(visited,graph,node,goal):
    visited.append(node)
    queue.append(node)
    goal_found = False
    while queue:
        print(f'the visited nodes are: {visited}')
        print(f'the bfs queue is: {queue}')
        m = queue.pop(0)
        print(m,end=' ')
        
        if m == goal:
            print('goal found')
            goal_found = True
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        
    return goal_found
    
graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}


found = bfs(visited,graph,"5","8")

if found:
    print('goal state was found')
else :
    print('goal state not found')