################################################################################
# We are given a graph (typically represented as an adjacency list), and we want to find all nodes connected to each node using DFS. 
# The goal is to start from each node, traverse the graph using DFS, and find all nodes that are reachable (connected) from that node.

# Graph:
# 0: [1, 2]
# 1: [0, 3, 4]
# 2: [0]
# 3: [1]
# 4: [1]

#  0 --- 1
#  |     |
#  2 --- 3
#        |
#        4
################################################################################


#-------------------------- DFS ------------------------------#
# This function takes in the graph, a current node, a visited array to track visited nodes, and a connectedNodes array to store all nodes that are connected to the current node.
# It marks the current node as visited and then recursively visits all unvisited neighbors.
# Find Connected Nodes Function (findConnectedNodes):
# 
# This function initializes a visited array (to keep track of whether a node has been visited during DFS).
# It iterates through all nodes in the graph and calls dfs on any node that hasn't been visited yet.
# It stores the connected nodes for each node in the connectedNodesDict.
# Graph Representation:
# 
# The graph is represented as an array of arrays (adjacency list). Each array element corresponds to a node, and the inner array contains the list of neighbors connected to that node.
# Output:
# 
# After the DFS is performed, the connectedNodesDict will contain each node as a key, and the value will be an array of nodes that are connected to it.
#-------------------------------------------------------------#
def dfs(graph, node, visited, connected_nodes):
    # Mark the current node as visited
    visited[node] = True
    connected_nodes.append(node)

    # Recurse on all the neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, connected_nodes)

def find_connected_nodes(graph):
    # Initialize a visited array to track visited nodes
    visited = [False] * len(graph)

    # Dictionary to store the list of connected nodes for each node
    connected_nodes_dict = {}

    # Perform DFS for each node
    for node in range(len(graph)):
        if not visited[node]:
            connected_nodes = []  # List to store the connected nodes for this component
            dfs(graph, node, visited, connected_nodes)
            # Store the connected component for the current node
            for n in connected_nodes:
                connected_nodes_dict[n] = connected_nodes

    return connected_nodes_dict

# Example graph as adjacency list
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Find connected nodes for each node
connected_nodes = find_connected_nodes(graph)

# Output the connected nodes for each node
for node, nodes in connected_nodes.items():
    print(f"Node {node} is connected to: {nodes}")


#-------------------------- BFS ------------------------------#
# Key Points:
#- Queue: BFS uses a queue to explore nodes level by level.
#- Visited Array: This ensures that nodes are not revisited.
#- Graph Representation: The graph is represented as an adjacency list, which is common in BFS and DFS implementations.
#
#Time Complexity: For an adjacency list representation of a graph with V vertices and E edges, BFS has a time complexity of O(V+E), where V is the number of vertices and E is the number of edges.
#
#Modifying for Directed Graphs:
#- If you're working with a directed graph, the BFS will only explore the nodes in the direction of the edges. The adjacency list for a directed graph might look like this:
#directedGraph = [
#    [1],    // Node 0 is connected to Node 1
#    [2],    // Node 1 is connected to Node 2
#    [3],    // Node 2 is connected to Node 3
#    [],     // Node 3 has no outgoing edges
#    [2]     // Node 4 is connected to Node 2
#]
#-------------------------------------------------------------#

from collections import deque

def bfs(graph, start_node):
    # Create a visited list to track visited nodes
    visited = [False] * len(graph)
    queue = deque([start_node])  # Initialize the queue with the start node
    connected_nodes = []

    visited[start_node] = True

    # Perform BFS
    while queue:
        node = queue.popleft()  # Dequeue the first node in the queue
        connected_nodes.append(node)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  # Enqueue the unvisited neighbor

    return connected_nodes

def find_connected_nodes(graph):
    connected_nodes_dict = {}

    # Perform BFS for each node
    for node in range(len(graph)):
        connected_nodes_dict[node] = bfs(graph, node)

    return connected_nodes_dict

# Example graph as adjacency list
graph = [
    [1, 2],    # Node 0 is connected to Node 1 and Node 2
    [0, 3, 4], # Node 1 is connected to Node 0, Node 3, and Node 4
    [0],       # Node 2 is connected to Node 0
    [1],       # Node 3 is connected to Node 1
    [1]        # Node 4 is connected to Node 1
]

# Find connected nodes for each node
connected_nodes = find_connected_nodes(graph)

# Output the connected nodes for each node
for node, nodes in connected_nodes.items():
    print(f"Node {node} is connected to: {nodes}")
