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
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C']
# }

# nodes = ['A', 'B', 'C', 'D', 'E', 'F']
# node_connections = [
#   ['A', 'B'],
#   ['A', 'C'],
#   ['B', 'D'],
#   ['B', 'E'],
#   ['C', 'F']
# ]


# adjacencyList = dict()
# for node in nodes:
#   adjacencyList[node] = []

# for edge in node_connections:
#   adjacencyList.get(edge[0]).append(edge[1])
#   adjacencyList.get(edge[1]).append(edge[0])

# print("Graph: ", adjacencyList)
# print("---------------")


# def BFS(graph, start):
#   visited = set()
#   queue = [start]
#   while len(queue) > 0:
#     node = queue.pop(0)
#     current_node = graph.get(node)
#     if node not in visited:
#       # Process the node (Here, just print it)
#       print(node, end=" ")
#       visited.add(node)
#     for neighbor in graph[node]:
#       if neighbor not in visited:
#         queue.append(neighbor)

# print("BFS Traversal:")
# BFS(graph, 'A')  # Output: A B C D E F
# print("---")
# BFS(graph, 'B')  # Output: B A D E C F
# print("---")
# BFS(graph, 'F')  # Output: F C A B D E
# print("---------------")


# def DFS(graph, node, visited=None):
#   if visited is None:
#     visited = set()
#   if node not in visited:
#     print(node)
#     visited.add(node)
#   for neighbor in graph[node]:
#     if neighbor not in visited:
#       DFS(graph, neighbor, visited)

# print(DFS(graph, 'A'))












nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
  ['A', 'B'],
  ['A', 'C'],
  ['B', 'D'],
  ['B', 'E'],
  ['C', 'F']
]


graph = dict()

for n in nodes:
  graph[n] = []

for e in edges:
  graph.get(e[0]).append(e[1])
  graph.get(e[1]).append(e[0])

#print(graph)
# {
#   'A': ['B', 'C'],
#   'B': ['A', 'D', 'E'],
#   'C': ['A', 'F'],
#   'D': ['B'],
#   'E': ['B'],
#   'F': ['C']
# }
  
def bfs(g, start):
  visited = set()
  queue = [start]
  while len(queue) > 0:
    node = queue.pop(0)
    if node not in visited:
      print(node, end=" ")
      visited.add(node)
    for neighbor in g[node]:
      if neighbor not in visited:
        queue.append(neighbor)

print(bfs(graph, 'A'))


def dfs(graph, node, visited=None):
  if visited is None:
    visited = set()
  if node not in visited:
    print(node, end=" ")
    visited.add(node)
  for neighbor in graph[node]:
    if neighbor not in visited:
      dfs(graph, neighbor, visited)

print(dfs(graph, 'A'))
