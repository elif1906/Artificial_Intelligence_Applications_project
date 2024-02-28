import heapq
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        for next_node in graph[node] - set(path):
            stack.append((next_node, path + [next_node]))

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        if node == goal:
            return path
        for next_node in graph[node] - set(path):
            queue.append((next_node, path + [next_node]))

def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node == goal:
            return path + [node]
        if node in visited:
            continue
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                next_node_cost = cost + heuristic(node, next_node)
                heapq.heappush(heap, (next_node_cost, next_node, path + [node]))

def print_menu():
    print("1. DFS (Depth First Search)")
    print("2. BFS (Breadth First Search)")
    print("3. A* (A Star)")
    print("4. Exit")

def draw_graph(graph, path=None):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
    
    if path:
        edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    
    plt.show()

def main():
    graph = {(0, 0): {(1, 2), (3, 1)},
             (1, 2): {(0, 0), (2, 2), (2, 4)},
             (2, 2): {(1, 2), (2, 4)},
             (2, 4): {(1, 2), (2, 2), (4, 3)},
             (3, 1): {(0, 0), (4, 3)},
             (4, 3): {(2, 4), (3, 1)}}

    start = (0, 0)
    goal = (4, 3)

    while True:
        print_menu()
        choice = input("Please enter an option: ")

        if choice == '1':
            path = dfs(graph, start, goal)
            print("DFS result:", path)
            draw_graph(graph, path)
        elif choice == '2':
            path = bfs(graph, start, goal)
            print("BFS result:", path)
            draw_graph(graph, path)
        elif choice == '3':
            path = astar(graph, start, goal)
            print("A* result:", path)
            draw_graph(graph, path)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
