// Heres a list of airports,
// and a list of routes connecting these airports, now represent this data as a graph.

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
/*
Can represent this two ways, a Matrix, or an Adjacency List.
A Matrix takes up more space, but is generally easier to visualize and represent because it is just a 2 dimensional array filled with ones and zeroes.
Here the matrix would have a lot of empty spaces because there are not a lot of airport relative to the possible combinations of paths.
A matrix would also be a lot slower to iterate over.
*/

const adjacencyList = new Map();

//define function that can add a node to the map
const addNode = (airport) => {
  adjacencyList.set(airport, []);
};

// add edge, undirected
const addEdge = (origin, destination) => {
  adjacencyList.get(origin).push(destination);
  adjacencyList.get(destination).push(origin);
};

//Create the graph
airports.forEach(addNode);
routes.forEach((route) => addEdge(...route));

console.log("adjacencyList: ", adjacencyList);
//-----------------------------------------//
//-----------------------------------------//
/*
// Can also (might be better) to encapsulate in a function. For Example:
function addNode(graph, airport) {
  graph.set(airport, []);
}

function addEdge(graph, origin, destination) {
  // (this called while looping through routes)
  // gets the matching route origin to airports, and adds the destination.
  // Gets the matching destination in route tp airports, and adds origin.
  graph.get(origin).push(destination);
  graph.get(destination).push(origin);
}

// create new Map here in function rather than globally and return it.
function createGraph(airports, routes) {
  const graph = new Map();
  airports.forEach((airport) => addNode(graph, airport));
  routes.forEach((route) => addEdge(graph, ...route));
  return graph;
}

const adjacencyListMatrix = createGraph(airports, routes);
console.log("adjacencyListMatrix: ", adjacencyListMatrix);
*/


//-----------------------------------------//
//-----------------------------------------//
// Graph search or traversal...Breadth First Search
const bfs = (start) => {
  // value in set may only occur once. We do this to prevent an infinite loop which would happen of this line was not here.
  const visited = new Set();

  const queue = [start];

  while (queue.length > 0) {
    const airport = queue.shift(); // mutates the queue..removes first element
    const destinations = adjacencyList.get(airport); // gets node currently on
    for (const destination of destinations) {
      //console.log(destination);
      if (destination === "BKK") {
        //check to see if current node is one we are looking for
        console.log("Found it!");
      }
      if (!visited.has(destination)) {
        // if Set does not contain the destination
        visited.add(destination); // add to set to  mark as visited
        queue.push(destination); // item only gets in queue if it has not been visited already
      }
    }
  }
};
bfs("PHX");

/*****************************************/
/*
DFS (Depth First Search)... more efficient way to search.
Instead of going through all the children...you go to first child, then its first child etc...until you find it,
then back track to top of graph and repeat.
*/

const dfs = (start, visited = new Set()) => {
  //console.log("START",start);
  visited.add(start);
  const destinations = adjacencyList.get(start);

  for (const destination of destinations) {
    if (destination === "BKK") {
      console.log("visited", visited);
      const steps = visited.size;
      console.log(`DFS found Bangkok in ${steps} steps`);
      return;
    }

    if (!visited.has(destination)) {
      dfs(destination, visited); // recursive call if a node has not been visited
    }
  }
};

dfs("PHX");

function dfs2(start, visited = new Set()) {
  //console.log(start)
  visited.add(start);
  const destinations = adjacencyList.get(start);

  for (const destination of destinations) {
    if (destination === "BKK") {
      console.log(`DFS found Bangkok`);
      return;
    }

    if (!visited.has(destination)) {
      dfs2(destination, visited);
    }
  }
}

dfs2("PHX");

/*
The recursive nature of this algorithm means that if a node has not been visited,
we call the function again, pushing it to the top of the call stack. Making the algorithm go deeper and deeper into the tree
until we find a match.That means that this function will continue to call itself recursively until all of the airports have been visited,
or until it finds Bangkok.

The DFS way only take three steps, or three function calls to find our route, as opposed to (8) in the previous one. (BFS)
*/
