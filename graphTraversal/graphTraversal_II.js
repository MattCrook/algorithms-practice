/*
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
*/

const nodes = ["A", "B", "C", "D", "E", "F"];
const edges = [
  ["A", "B"],
  ["A", "C"],
  ["B", "D"],
  ["B", "E"],
  ["C", "F"],
];

const graph = new Map();

nodes.forEach((node) => {
  graph.set(node, []);
});

edges.forEach((edge) => {
  graph.get(edge[0]).push(edge[1]);
  graph.get(edge[1]).push(edge[0]);
});

console.log("Adjacency List:");
console.log(graph);
/*
Adjacency List:
Map(6) {
  'A' => [ 'B', 'C' ],
  'B' => [ 'A', 'D', 'E' ],
  'C' => [ 'A', 'F' ],
  'D' => [ 'B' ],
  'E' => [ 'B' ],
  'F' => [ 'C' ]
}*/

//********************* BFS ******************//
const bfs = (graph, start) => {
  const visited = new Set();
  const queue = [start];
  while (queue.length > 0) {
    const node = queue.shift();
    if (!visited.has(node)) {
      console.log(node);
      visited.add(node);
    }
    const neighbors = graph.get(node);
    for (const neighbor of neighbors) {
      if (!visited.has(neighbor)) {
        queue.push(neighbor);
      }
    }
  }
};

console.log(bfs(graph, "A"));
console.log(bfs(graph, "B"));
console.log(bfs(graph, "F"));

//********************* DFS ******************//
const dfs = (graph, node, visited = new Set()) => {
  if (!visited.has(node)) {
    console.log(node);
    visited.add(node);
  }

  const neighbors = graph.get(node);
  for (const neighbor of neighbors) {
    if (!visited.has(neighbor)) {
      dfs(graph, neighbor, visited);
    }
  }
};

console.log(dfs(graph, "A"));
console.log(dfs(graph, "B"));
console.log(dfs(graph, "F"));
