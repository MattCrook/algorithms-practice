/*
################################################################################
We are given a graph (typically represented as an adjacency list), and we want to find all nodes connected to each node using DFS and BFS. 
The goal is to start from each node, traverse the graph using DFS, and find all nodes that are reachable (connected) from that node.

Graph:
0: [1, 2]
1: [0, 3, 4]
2: [0]
3: [1]
4: [1]

 0 --- 1
 |     |
 2 --- 3
       |
       4
################################################################################
*/


//***************************** DFS *******************************//
/*
This function takes in the graph, a current node, a visited array to track visited nodes, and a connectedNodes array to store all nodes that are connected to the current node.
It marks the current node as visited and then recursively visits all unvisited neighbors.
Find Connected Nodes Function (findConnectedNodes):

This function initializes a visited array (to keep track of whether a node has been visited during DFS).
It iterates through all nodes in the graph and calls dfs on any node that hasn't been visited yet.
It stores the connected nodes for each node in the connectedNodesDict.
Graph Representation:

The graph is represented as an array of arrays (adjacency list). Each array element corresponds to a node, and the inner array contains the list of neighbors connected to that node.
Output:

After the DFS is performed, the connectedNodesDict will contain each node as a key, and the value will be an array of nodes that are connected to it.
*/
//***************************** //
function dfs(graph, node, visited, connectedNodes) {
  // Mark the current node as visited
  visited[node] = true;
  connectedNodes.push(node);

  // Recurse on all the neighbors
  for (let neighbor of graph[node]) {
    if (!visited[neighbor]) {
      dfs(graph, neighbor, visited, connectedNodes);
    }
  }
}

function findConnectedNodes(graph) {
  // Initialize a visited array to track visited nodes
  const visited = new Array(graph.length).fill(false);

  // Object to store the connected nodes for each node
  const connectedNodesDict = {};

  // Perform DFS for each node
  for (let node = 0; node < graph.length; node++) {
    if (!visited[node]) {
      const connectedNodes = []; // List to store the connected nodes for this component
      dfs(graph, node, visited, connectedNodes);

      // Store the connected component for the current node
      for (let n of connectedNodes) {
        connectedNodesDict[n] = connectedNodes;
      }
    }
  }

  return connectedNodesDict;
}

// Example graph as adjacency list
let graphDFS = [
  [1, 2], // Node 0 is connected to Node 1 and Node 2
  [0, 3, 4], // Node 1 is connected to Node 0, Node 3, and Node 4
  [0], // Node 2 is connected to Node 0
  [1], // Node 3 is connected to Node 1
  [1], // Node 4 is connected to Node 1
];

// Find connected nodes for each node
const connectedNodes = findConnectedNodes(graphDFS);

// Output the connected nodes for each node
for (const node in connectedNodes) {
  console.log(`Node ${node} is connected to: ${connectedNodes[node]}`);
}

console.log("----------------------------------------")

//***************************** BFS *******************************//
/*
Key Points:
- Queue: BFS uses a queue to explore nodes level by level.
- Visited Array: This ensures that nodes are not revisited.
- Graph Representation: The graph is represented as an adjacency list, which is common in BFS and DFS implementations.

Time Complexity: For an adjacency list representation of a graph with V vertices and E edges, BFS has a time complexity of O(V+E), where V is the number of vertices and E is the number of edges.

Modifying for Directed Graphs:
- If you're working with a directed graph, the BFS will only explore the nodes in the direction of the edges. The adjacency list for a directed graph might look like this:
const directedGraph = [
    [1],    // Node 0 is connected to Node 1
    [2],    // Node 1 is connected to Node 2
    [3],    // Node 2 is connected to Node 3
    [],     // Node 3 has no outgoing edges
    [2]     // Node 4 is connected to Node 2
];
*/
//***************************** //
function bfs(graph, startNode) {
  const visited = new Array(graph.length).fill(false);
  const queue = [startNode];
  const connectedNodes = [];

  visited[startNode] = true;

  while (queue.length > 0) {
    const node = queue.shift(); // Dequeue the first node in the queue
    connectedNodes.push(node);

    // Explore all neighbors of the current node
    for (let neighbor of graph[node]) {
      if (!visited[neighbor]) {
        visited[neighbor] = true;
        queue.push(neighbor); // Enqueue unvisited neighbors
      }
    }
  }

  return connectedNodes;
}

function findConnectedNodes(graph) {
  const connectedNodesDict = {};

  // Perform BFS for each node
  for (let node = 0; node < graph.length; node++) {
    connectedNodesDict[node] = bfs(graph, node);
  }

  return connectedNodesDict;
}

// Example graph as adjacency list
const graphBFS = [
  [1, 2], // Node 0 is connected to Node 1 and Node 2
  [0, 3, 4], // Node 1 is connected to Node 0, Node 3, and Node 4
  [0], // Node 2 is connected to Node 0
  [1], // Node 3 is connected to Node 1
  [1], // Node 4 is connected to Node 1
];

// Find connected nodes for each node
const connectedNodesBFS = findConnectedNodes(graphBFS);

// Output the connected nodes for each node
for (const node in connectedNodesBFS) {
  console.log(`Node ${node} is connected to: ${connectedNodesBFS[node]}`);
}
