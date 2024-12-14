"""
# Example Graph:
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F
# This graph can be represented as an adjacency list.


# Find all nodes connected to each node. 
# E.g. 
#  - A is connected to A, B, C, D, E, F
#  - B is connected to A, D, E
#  - C is connected to A, F
#  - D is connected to B
#  - E is connected to B
#  - F is connected to C

1) Create Adjacency List To represent Graph
2) Find all connected Nodes per each node (node passed in, output all connected nodes.)

Example 1.
# Input A
# Output: A B C D E F


"""

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

print("Graph: ", adjacencyList)
print("---------------")


def BFS(graph, start):
  visited = set()
  queue = [start]
  while len(queue) > 0:
    node = queue.pop(0)
    #current_node = graph.get(node)
    if node not in visited:
      # Process the node (Here, just print it)
      print(node, end=" ")
      visited.add(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

print("BFS Traversal:")
BFS(adjacencyList, 'A')  # Output: A B C D E F
print("---")
BFS(adjacencyList, 'B')  # Output: B A D E C F
print("---")
BFS(adjacencyList, 'F')  # Output: F C A B D E
print("---------------")
