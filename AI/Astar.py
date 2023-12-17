graph = {
    "A": {"B": 9, "C": 4, "D": 7},
    "B": {"E": 11},
    "C": {"E": 17, "F": 12},
    "D": {"F": 14},
    "E": {"Z": 5},
    "F": {"Z": 9},
}

# Define the heuristic values for A* search - h(n) for each node
heuristic = {"A": 21, "B": 14, "C": 18, "D": 18, "E": 5, "F": 8, "Z": 0}
start_node = input("Enter Start Node: ")  # this is also start node at the beginning
curr_node = start_node
goal_node = input("Enter Goal Node: ")

def costFormula(path, node):
    g = 0
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        g += graph[from_node][to_node]
    
    h = heuristic[node]
    return g + h

close_list = []
open_list = []

open_list.append([start_node, heuristic[start_node], [start_node]])

try:
    while open_list:
        open_list.sort(key=lambda x: x[1])
        current_node, current_cost, current_path = open_list.pop(0)
        
        close_list.append(current_path)
        
        if current_node == goal_node:
            print(f'Optimized path from {start_node} to {goal_node} is {current_path} and distance is {current_cost}')
            break
        
        print(f'Currently at node: {current_node}')
        
        for neighbour in graph[current_node]:
            new_path = current_path + [neighbour]
            new_cost = costFormula(new_path, neighbour)
            open_list.append([neighbour, new_cost, new_path])
        
        print(f'Open list is: {open_list}')
        print(f'Closed list is: {close_list}')
        
except Exception as e:
    print('Something went wrong', e)


