from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()

        print(f"open: {list(visited)}", end="   ")
        print(f"close: {node}", end="   ")
        print(f"goal-test: {node == goal}")

        if node == goal:
            print("\nGoal node found.")
            return True

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [node]))

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

print("\nBFS traversal:")
if not bfs(graph, start_node, goal_node):
    print("Goal node not found.")
