def dfs(graph, node, goal, visited=None):
    if visited is None:
        visited = set()
    
    print(f"open: {list(visited)}", end="   ")
    print(f"close: {node}", end="   ")
    print(f"goal-test: {node == goal}")

    if node == goal:
        print("\nGoal node found.")
        return True

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False

def build_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        source, destination = input("Enter edge (source destination): ").split()
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)
        
       
        if destination not in graph:
            graph[destination] = []
        graph[destination].append(source)
    
    return graph


graph = build_graph()
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

print("\nDFS traversal:")
if not dfs(graph, start_node, goal_node):
    print("Goal node not found.")
