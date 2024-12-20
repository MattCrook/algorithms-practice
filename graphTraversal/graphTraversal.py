##############################################################
# Heres a list of airports, and a list of routes connecting these airports, now represent this data as a graph.
# Perform BFS and DFS to find all routes per Airport.
#
# ------------ #
# CHALLENGE:
# - Given an airport as input (e.g. "PHX"), find how many "steps" it takes for the algorithm to find a destination.
# - For example, we have "MEX" and want to find how many steps it takes to find "EZE", and finds in (3 and 7) steps (bfs), and 9 steps (dfs).
# ------------ #

airports = "PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM".split(" ");

routes = [
  ["PHX", "LAX"],
  ["PHX", "JFK"],
  ["JFK", "OKC"],
  ["JFK", "HEL"],
  ["JFK", "LOS"],
  ["MEX", "LAX"],
  ["MEX", "BKK"],
  ["MEX", "LIM"],
  ["MEX", "EZE"],
  ["LIM", "BKK"],
];

##############################################################

#---------- Create Adjacency List ----------#
def createAdjacencyList(nodes, edges):
  graph = dict()

  for n in nodes:
    graph[n] = []


  for e in edges:
    graph.get(e[0]).append(e[1])
    graph.get(e[1]).append(e[0])

  return graph

adjacencyList = createAdjacencyList(airports, routes)
print(adjacencyList)
print("----------------")


# couple different ways to format the adjacencyList so it is more easily readable.
# Since Python doesn't give us a nice output like a Javascript Map() does.
def print_adjacencyList(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

print_adjacencyList(adjacencyList)
print("----------------")

# One liners
print("\n".join("{}\t{}".format(k, v) for k, v in adjacencyList.items()))
print("----------------")
print("\n".join("{}\t{}".format(k, v) for k, v in sorted(adjacencyList.items(), key=lambda t: str(t[0]))))
print("----------------")

import pprint
# pprint module (Pretty Print) included in Python. It can be used to either print the object, or format a nice string version of it.

# Prints the nicely formatted dictionary
pprint.pprint(adjacencyList)
# Sets 'pretty_dict_str' to the formatted string value
# pretty_dict_str = pprint.pformat(adjacencyList)
print("----------------------")

# Output is in one way or another this...
'''
{
  'PHX': ['LAX', 'JFK'], 
  'BKK': ['MEX', 'LIM'], 
  'OKC': ['JFK'], 
  'JFK': ['PHX', 'OKC', 'HEL', 'LOS'], 
  'LAX': ['PHX', 'MEX'], 
  'MEX': ['LAX', 'BKK', 'LIM', 'EZE'], 
  'EZE': ['MEX'], 
  'HEL': ['JFK'], 
  'LOS': ['JFK'], 
  'LAP': [], 
  'LIM': ['MEX', 'BKK']
}
'''

#---------------- BFS -----------------#
def bfs(start, dest):
  visited = set()
  queue = [start]

  while len(queue) > 0:
    airport = queue.pop(0) # mutate the queue - remove first element.
    destinations = adjacencyList.get(airport) # get the node we are currently on.
    for destination in destinations:
      if destination == dest:  # check to see if current node is one we are looking for
        print(f'Found {dest} in {len(visited)} steps using BFS')
      if destination not in visited:
        visited.add(destination)
        queue.append(destination)



print(bfs("PHX", "BKK"))
print(bfs("MEX", "EZE"))
print("-----------------")

#---------------- DFS -----------------#

def dfs(start, dest, visited=set()):
  visited.add(start)
  destinations = adjacencyList.get(start)
  for destination in destinations:
    if destination == dest:
      print(f'Found {dest} in {len(visited)} steps using DFS.')
      return
    if destination not in visited:
      dfs(destination, dest, visited)

print(dfs("PHX", "BKK"))
print(dfs("MEX", "EZE"))
