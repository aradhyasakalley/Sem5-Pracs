def dfs(graph,src,path=[]):
    if src not in path:
        path.append(src)
        if src == goal_state:
            path.append("(GOAL)")
            return path
        if src not in graph:
            return path
        
        for neighbour in graph[src]:
            path = dfs(graph,neighbour,path)
            if "(GOAL)" in path:
                break
    return path

graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}
goal_state = "8"
path = dfs(graph,"5")
print(" -> ".join(path))
if "(GOAL)" in path:
    print('goal node found')
else :
    print('goal node not found')
    