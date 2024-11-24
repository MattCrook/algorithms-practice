//------------------------------------------//
// Heres a list of airports and a list of routes connecting these airports, now represent this data as a graph.
//------------------------------------------//

const airports = "PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM".split(" ");

const routes = [
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

function addNode(graph, airport) {
  graph.set(airport, []);
}

function addEdge(graph, origin, destination) {
  graph.get(origin).push(destination);
  graph.get(destination).push(origin);
}

/*
airports.forEach((airport) => addNode(graph, airport));
Creates:
Map(11) {
  'PHX' => [],
  'BKK' => [],
  'OKC' => [],
  'JFK' => [],
  'LAX' => [],
  'MEX' => [],
  'EZE' => [],
  'HEL' => [],
  'LOS' => [],
  'LAP' => [],
  'LIM' => []
}
    */
function createGraph(airports, routes) {
  const graph = new Map();
  airports.forEach((airport) => addNode(graph, airport));
  routes.forEach((route) => addEdge(graph, ...route));
  return graph;
}

const adjacencyListMatrix = createGraph(airports, routes);
console.log("Matrix: ", adjacencyListMatrix);
console.log("-----------------------------");

//-------------------------------------------------------------------//
/*
Now given this directed graph, what are two ways we can search for whether this is a route to or from a given airport?
- Design these algorithm(s), and explain what the benefits of each are.

Depth-First Search
- We start at the route or another arbitrarily selected note and explore each branch completely before moving onto the next branch.
- That is, we go deep first before we go wide.

Breadth-First Search
- We start at the route or another arbitrarily selected note and explore each neighbor before going onto any of their children.
- That is we go wide before going deep

DFS ss often preferred if we want to visit every note in the graph.
Both will work, but DFS search is a bit simpler.
However, if we want to find the shortest path or any path between two notes, BFS is generally better.
*/
//------------------------------------------------------//

// PROBLEM
// From a given starting airport, find the number of connecting flights (steps) to get to Bangkok (BKK).
//  - Search the adjacencyListMatrix created above and record the number of steps.



/*
DFS
Code Explanation
- Start with a starting point, and empty Set to keep track of visited nodes.
- every time you visit a node, add it to the visited Set
- get the full list of destinations from the target destination from the Adjacency Matrix
  - Iterate through the destinations at where you started.
- search for your target destination
- if successful find, return the destination and number of steps.
- if not, make a recursive call if node has not been visited, and continue searching until found.

destinations Example:
dest [ 'LAX', 'JFK' ]
dest [ 'PHX', 'MEX' ]
dest [ 'LAX', 'BKK', 'LIM', 'EZE' ]
Found BKK in 3 steps.
*/
const DFS = (adjacencyMatrix, start, target, visited = new Set()) => {
  visited.add(start);
  const destinations = adjacencyMatrix.get(start);
  for (const destination of destinations) {
    if (destination === target) {
      const steps = visited.size;
      console.log(`Found ${target} in ${steps} steps using DFS.`);
      return;
    }
    if (!visited.has(destination)) {
      DFS(adjacencyMatrix, destination, target, visited);
    }
  }
};

DFS(adjacencyListMatrix, "PHX", "BKK");
DFS(adjacencyListMatrix, "JFK", "BKK");
DFS(adjacencyListMatrix, "MEX", "BKK");
console.log("-----------------------------");

//------------------------------------------------------//

/*
BFS
Code Explanation
  - Create new Set to keep track of visited nodes, as well as prevent an infinite loop which would happen if not a Set.
  - Create a queue, (to loop over), starting with our starting point.
  - While the queue length is greater than zero, remove the first element and search the adjacencyListMatrix for that airport - to get its destinations.
  - Loop over the destinations, and find a match to our target.
  - if no match, mark the destination as visited, and add the destination to the queue (only if it has been visited).

While loop (visited), example:
Set(0) {}
Set(2) { 'LAX', 'JFK' }
Set(4) { 'LAX', 'JFK', 'PHX', 'MEX' }
Set(7) { 'LAX', 'JFK', 'PHX', 'MEX', 'OKC', 'HEL', 'LOS' }
Set(7) { 'LAX', 'JFK', 'PHX', 'MEX', 'OKC', 'HEL', 'LOS' }
Found BKK in 7 steps using BFS.

Queue example:
[ 'PHX' ]
[ 'LAX', 'JFK' ]
[ 'JFK', 'PHX', 'MEX' ]
[ 'PHX', 'MEX', 'OKC', 'HEL', 'LOS' ]
[ 'MEX', 'OKC', 'HEL', 'LOS' ]
Found BKK in 7 steps using BFS.
*/
const BFS = (adjacencyListMatrix, start, target) => {
  const visited = new Set();
  const queue = [start];
  while (queue.length > 0) {
    const airport = queue.shift();
    const destinations = adjacencyListMatrix.get(airport);
    for (const destination of destinations) {
      if (destination === target) {
        const steps = visited.size;
        console.log(`Found ${target} in ${steps} steps using BFS.`);
        return;
      }
      if (!visited.has(destination)) {
        visited.add(destination);
        queue.push(destination);
      }
    }
  }
};

BFS(adjacencyListMatrix, "PHX", "BKK");
BFS(adjacencyListMatrix, "JFK", "BKK");
BFS(adjacencyListMatrix, "MEX", "BKK");
console.log("-----------------------------");
