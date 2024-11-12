/*
Doubly Linked List Class Implementation

A Doubly Linked List is similar to a singly linked list, but with an important difference: each node has two references (or pointers). One pointer points to the next node in the sequence, while the other points to the previous node. This allows traversal of the list in both directions (forward and backward).

Components of a Doubly Linked List:
 - Node: Each node has three parts:
 - data: The value of the node.
 - next: A reference to the next node in the list.
 - prev: A reference to the previous node in the list.
 - Doubly Linked List: The list itself is a collection of nodes with a reference to both the first (head) and last (tail) nodes.

Node Class:
   - Each node contains data, next, and prev. next points to the next node, while prev points to the previous node.

DoublyLinkedList Class:
  - append(data): Adds a new node with the given data at the end of the list.
  - insertAt(data, index): Inserts a new node at the specified index. This method handles cases for inserting at the beginning, middle, and end.
  - removeAt(index): Removes the node at the given index.
  - printForward(): Traverses and prints the list from head to tail.
  - printBackward(): Traverses and prints the list from tail to head.
  - getSize(): Returns the number of nodes in the list.
  - isEmpty(): Checks if the list is empty.
  - find(data): Finds the node containing the specified data.
Time Complexity:
  - Append: O(1) – We directly append to the tail.
  - Insert At Index: O(n) – We may need to traverse to the index.
  - Remove At Index: O(n) – We may need to traverse to the index.
  - Find: O(n) – We need to traverse the list to find the data.
*/

class Node {
  constructor(data) {
    this.data = data; // The value of the node
    this.next = null; // Points to the next node in the list (default is null)
    this.prev = null; // Points to the previous node in the list (default is null)
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null; // Points to the first node
    this.tail = null; // Points to the last node
    this.size = 0; // Tracks the number of nodes in the list
  }

  // Add a new node at the end of the list
  append(data) {
    const newNode = new Node(data);

    if (this.size === 0) {
      // If the list is empty, the new node becomes both the head and the tail
      this.head = newNode;
      this.tail = newNode;
    } else {
      // Otherwise, append the new node after the tail
      this.tail.next = newNode; // Link current tail's next to the new node
      newNode.prev = this.tail; // Link the new node's prev to the current tail
      this.tail = newNode; // Update the tail to the new node
    }

    this.size++;
  }

  // Insert a node at a specific position
  insertAt(data, index) {
    if (index < 0 || index > this.size) return; // Out of bounds

    const newNode = new Node(data);

    if (index === 0) {
      // Insert at the beginning
      newNode.next = this.head;
      if (this.head) this.head.prev = newNode; // Update previous head's prev to new node
      this.head = newNode; // New node becomes the head
      if (this.size === 0) this.tail = newNode; // If list was empty, tail also becomes new node
    } else if (index === this.size) {
      // Insert at the end (same as append)
      this.append(data);
      return;
    } else {
      // Insert at a specific index
      let current = this.head;
      let count = 0;

      // Traverse to the given index
      while (count < index) {
        current = current.next;
        count++;
      }

      // Insert the new node between current and current.prev
      newNode.prev = current.prev;
      newNode.next = current;
      current.prev.next = newNode;
      current.prev = newNode;
    }

    this.size++;
  }

  // Remove a node from the list by its index
  removeAt(index) {
    if (index < 0 || index >= this.size) return; // Out of bounds

    let current = this.head;

    if (index === 0) {
      // Remove the head node
      if (this.head === this.tail) {
        this.head = null;
        this.tail = null;
      } else {
        this.head = this.head.next;
        this.head.prev = null;
      }
    } else if (index === this.size - 1) {
      // Remove the tail node
      this.tail = this.tail.prev;
      this.tail.next = null;
    } else {
      // Remove from the middle
      let count = 0;
      while (count < index) {
        current = current.next;
        count++;
      }

      // Adjust the pointers to exclude the current node
      current.prev.next = current.next;
      current.next.prev = current.prev;
    }

    this.size--;
  }

  // Print the list from head to tail (forward traversal)
  printForward() {
    let current = this.head;
    let result = [];
    while (current) {
      result.push(current.data);
      current = current.next;
    }
    console.log(result.join(" <-> "));
  }

  // Print the list from tail to head (backward traversal)
  printBackward() {
    let current = this.tail;
    let result = [];
    while (current) {
      result.push(current.data);
      current = current.prev;
    }
    console.log(result.join(" <-> "));
  }

  // Get the size of the list
  getSize() {
    return this.size;
  }

  // Check if the list is empty
  isEmpty() {
    return this.size === 0;
  }

  // Find a node by its value
  find(data) {
    let current = this.head;
    while (current) {
      if (current.data === data) {
        return current; // Return the node if found
      }
      current = current.next;
    }
    return null; // Return null if not found
  }
}

const list = new DoublyLinkedList();

list.append(10);
list.append(20);
list.append(30);

console.log("Size of list:", list.getSize()); // Size of list: 3
list.printForward(); // 10 <-> 20 <-> 30
list.printBackward(); // 30 <-> 20 <-> 10

list.insertAt(15, 1); // Insert 15 at index 1
list.printForward(); // 10 <-> 15 <-> 20 <-> 30

list.removeAt(2); // Remove element at index 2 (which is 20)
list.printForward(); // 10 <-> 15 <-> 30

console.log("Finding 15:", list.find(15)); // Node { data: 15, next: Node { data: 30, next: null, prev: [Circular] }, prev: Node { data: 10, next: [Circular], prev: null } }
console.log("Finding 100:", list.find(100)); // null
