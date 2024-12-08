# Data Structures and Algorithms

Collection of coding algorithms and data structures, written in Javascript and Python, as well as problems / challenges using these algorithms (***See [challenges Readme](./challenges/README.md)***). Formatted in what you might see in LeetCode or interview questions.

----

##### This repository coincides with my blog post on this subject. Please refer to that for more in depth details and explanation of various algorithms:
* ##### [https://matt-crook.com/blog_posts/algorithms](https://matt-crook.com/blog_posts/algorithms)

----


##### Algorithms / Data Structures Include:
* Graph Traversal
* LinkedList
* Fizzbuzz
* Various Counting Algorithms
* Various Shuffling Algorithms
* Finding Sums of Integers
* String Manipulation
* Sorting Algorithms
* Searching Algorithms
* Fibonacci Sequence
* Binary Search Algorithm
* Circular Buffer Algorithms
* and more...
* [Challenges](./challenges/)

### Extra/ Random / Docs:
##### Python:
- https://github.com/heineman/python-data-structures
- https://docs.python.org/3/library/collections.html#deque-recipes
- https://www.codecademy.com/resources/blog/advanced-python-code-challenges/

<br>

<!-- ## Graph Search (BFS and DFS)

[Challenge Example](./challenges/javascript/adjancencyMatrix.js)

[Example Graph Traversal](./graphTraversal/)

#### Adjacency List
An adjacency list is the most common common way to represent a graph. Every vertex (or node) stores a list of adjacent vertices. In an undirected graph, an edge like `(a, b)` would be stored twice: once in `a's` adjacent vertices, and once in `b's` adjacent vertices.

![adjacency-list](./media/adjacency-list.png)


#### Adjacency Matrix

An adjacency matrix is `N x N` boolean matrix (where `N` is the number of nodes), where a `true` value at `matrix[i][j] ` indicates an edge from node `i` to node `j`. You can also use an integer matrix with zeros and ones.

* In an undirected graph, an adjacency matrix will be symmetric. In a directed graph, it will not necessarily be.

The graph algorithms that are used on adjacency lists can be performed with adjacency matrices, but they may be somewhat less efficient. In the adjacency list representation, you can easily iterate through the neighbors of a node. In the adjacency matrix representation, you will need to iterate through all the nodes to identify a node's neighbors.

![adjacency-matrix](./media/adjacency-matrix.png)

##### Algorithms

Two common ways to search a graph are ***Depth-First Search*** and ***Breath-First Search***.

[Example](./binarySearch/search.js)

In Depth-First Search (DFS), we start at the root (or another arbitrarily selected node) and explore each branch completely before moving onto the next branch. That is, we go deep first (hence the name depth- first search) before we go wide.


In Breath-First Search, we start at the root (or another arbitrarily selected note) and explore each neighbor before going onto any of their children. That is, we go wide (hence the name breath- first) before we go deep.

Breath-First Search (BFS) and Depth-First Search (DFS) tend to be used in different scenarios.

* DFS is often preferred if we want to visit every node in the graph. Both will work fine but depth first search is a bit simpler.
* However, if we want to find the shortest path or just any path between two notes BFS is generally better.


<br>

## Stacks

[Example](./stacksAndQueues/stack.js)

The stack data structure is precisely what it sounds like: a stack of data. In certain types of scenarios, it can be favorable to store data in a stack rather than in an array. A stack uses LIFO *(last-in, first- out)* ordering. That is, as in a stack of dinner plates. The most recent item added to the stack is the first item to be removed.

Unlike an array, a stack doesn't offer a consent-constant time access to the `i`th item. However, it does allow constant-time adds and removes as it doesn't require shifting elements around.

One case where stacks are often useful is in certain recursive algorithms. Sometimes you need to push temporary data onto a stack as you recurse, but then remove them as you backtrack (for example, because the recursive check failed.) A stack offers an intuitive way to do this. A stack can also be used to implement a recursive algorithm iteratively.

<br>

## Queues

[Example](./stacksAndQueues/queue.js)

A Queue implements FIFO *(first-in, first-out)* ordering. 
As in a line or queue at a ticket stand, items are removed from the data structure in the same order that they are added.

A queue can also be implemented with a linked list. In fact, they are essentially the same thing as long as items are added and removed from opposite sides.

One thing to note with a queue is, it is especially easy to mess up the updating of the first and last nodes.

One place are often used in breadth-first search, or an implementing a cache. In breadth-first search for example, we use a queue to store a list of nodes that we need to process. Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process nodes in the order in which they are viewed.

<br>

## HashMap

*(https://levelup.gitconnected.com/java-hashmap-explained-a601c48ddc44)*

[Example Python](./challenges/python/hashmap_ransomNote.py)

[Example Javascript](./challenges/javascript/hashmapRansomNote.js)

[Example Two Sum](./challenges/javascript/twoSum.js)

A HashMap or Hash Table is a data structure that maps keys to values for highly efficient lookups. There are a number of ways of implementing this.
A simple implementation is we can use an array of linked lists, and a hash code function.

Alternatively, we can implement a look up system with a balanced binary search tree. The advantage of this is potentially using less space since, we no longer allocate a large array. We can also iterate through the keys in order; which can also be useful sometimes.

<br>

## LinkedLists

[Examples](./linkedList/)


A Linked List is a data structure that represents a sequence of nodes. In a singly Linked List, each Node points to the next Node in the Linked List. A doubly Linked List gives each Node pointers to both the next Node and the previous Node. Unlike an array, a linked list does not provide constant time access to a particular index within the list.

<br>

## Fibonacci

[Examples](./fibonacci/)

The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. It starts with 0 and is followed by 1.


<br>

## Circular Buffer

[Examples](./circularBuffer/)

[Challenge Example](./challenges/python/circlular_buffer.py)

A a circular buffer (or circular queue, cyclic buffer or ring buffer) is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end. This structure lends itself easily to buffering data streams. The useful property of a circular buffer is that it does not need to have its elements shuffled around when one is consumed. -->
