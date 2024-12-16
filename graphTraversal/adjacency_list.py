"""
SIMPLE EXAMPLE PROBLEM


Example Graph:
     A
    /
   B -- C -- E
  /
 D


Example Problem:
This graph can be represented as an adjacency list.

1) Find all nodes connected to each node.
 - Create Adjacency List To represent Graph and Find all connected Nodes per each node.
"""


# STEP 01
# - create data structure(s) representing the nodes and edges.
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [
  ['A', 'B'],
  ['B', 'D'],
  ['B', 'C'],
  ['C', 'E']
]

# Create the Adjacency List.
def initAdjacencyList(nodes, edges):
  """
  Output will look like this, with each node and its corresponding edges.
  {
    'A': ['B'], 
    'B': ['A', 'D', 'C'], 
    'C': ['B', 'E'], 
    'D': ['B'], 
    'E': ['C']
  }
  """
  graph = dict()

  # set each node as a key in map/ dict.
  for n in nodes:
    graph[n] = []

  # for each of the edges, get the node (key), and append the corresponding edge.
  for e in edges:
    graph.get(e[0]).append(e[1])
    graph.get(e[1]).append(e[0])

  return graph


adj_list = initAdjacencyList(nodes, edges)
print("Graph: ", adj_list) # printing the whole graph here just to show it. Not necessary.

# function to return the edges of the Node (passed in).
def findConnected(graph, start):
  return graph[start]


print(findConnected(adj_list, 'B')) # ['A', 'D', 'C']
