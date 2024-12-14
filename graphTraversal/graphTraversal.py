
############################  Graph Traversal Algorithms #######################################
# Breadth-First Search (BFS):
# - BFS explores all the neighbors of a node before moving on to the next level neighbors.
# - It uses a queue data structure to manage the order of node visits.
# - It is commonly used for finding the shortest path in an unweighted graph, level-order traversal, and searching in a graph.
# Depth-First Search (DFS):
# - DFS explores as far as possible along each branch before backtracking. 
# - It uses a stack data structure (or recursion) to manage the node visits.
# - DFS can be used for path-finding, cycle detection, topological sorting, and exploring all possible paths.
#
# Example Graph:
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F
# This graph can be represented as an adjacency list:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Find all nodes connected to each node.
# E.g.
#  - A is connected to A, B, C, D, E, F
#  - B is connected to A, D, E
#  - C is connected to A, F
#  - D is connected to B
#  - E is connected to B
#  - F is connected to C

# 1) Create Adjacency List To represent Graph (already done...)
# 2) Find all connected Nodes per each node (node passed in, output all connected nodes.)

# Example 1.
# Input A
# Output: A B C D E F


################################################################################

#---- If graph wasn't given to us, can create our adjacency list like this ----#
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
node_connections = [
  ['A', 'B'],
  ['A', 'C'],
  ['B', 'D'],
  ['B', 'E'],
  ['C', 'F']
]

adjacencyList = dict()
for node in nodes:
  adjacencyList[node] = []

for edge in node_connections:
  adjacencyList.get(edge[0]).append(edge[1])
  adjacencyList.get(edge[1]).append(edge[0])

print(adjacencyList)


#-------- Breadth-First Search (BFS) --------------#
# BFS visits nodes level by level, using a queue to keep track of the next node to visit.
#
# BFS Algorithm:
# Start at the root (or any arbitrary node).
# Visit the node and add all its neighbors to the queue.
# Dequeue a node from the front of the queue and repeat the process for its neighbors.
# Continue until all reachable nodes are visited.
#
# Explanation:
# - BFS starts from node 'A' and explores all its neighbors, 'B' and 'C'.
# - Then, it moves to 'B' (first neighbor of 'A') and explores its neighbors ('A', 'D', 'E').
# - It continues this process level by level.
#----------------------------------------#
#from collections import deque

def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = [start]  # Initialize queue with start node
    #queue = deque([start])  # Initialize queue with start node

    while queue:
        node = queue.popleft()  # Dequeue a node

    while len(queue) > 0:
        node = queue.pop(0)  # Dequeue a node
        #node = queue.popleft()
        if node not in visited:
            print(node, end=" ")  # Process the node (Here, just print it)
            visited.add(node)  # Mark the node as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, 'A')  # Output: A B C D E F
# bfs(graph, 'B')  # Output: B A D E C F
# bfs(graph, 'F')  # Output: F C A B D E
print("--------------------")


# ----------------- Depth-First Search (DFS) --------------#
# DFS explores as deep as possible along a branch before backtracking. It uses a stack (either explicitly or via recursion).
#
# DFS Algorithm:
# - Start from the root (or any arbitrary node).
# - Visit the node and explore one of its neighbors.
# - Repeat the process for the next node and continue until there are no more neighbors to visit (backtrack).
# - Once all the neighbors of a node are explored, backtrack to the previous node and continue.
#
# Explanation:
# - DFS starts from node 'A' and explores as far as possible along the branch starting from 'B'.
# - After visiting 'D', it backtracks to 'B', then explores 'E'.
# - After exploring all neighbors of 'B', DFS backtracks to 'A' and explores 'C', then 'F'.
#----------------------------------------#
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set

    if node not in visited:
        print(node, end=" ")  # Process the node (Here, just print it)
        visited.add(node)  # Mark the node as visited

        # Recur for all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

# Example usage:
print("DFS Traversal:")
dfs(graph, 'A')  # Output: A B D E C F
print("--------------------")
