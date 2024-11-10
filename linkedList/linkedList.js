/*
Implementation of a Singly Linked List

A linked list is a data structure where each element (node) contains a value and a reference (or link) to the next element in the sequence. Linked lists are commonly used when you need to insert and delete elements efficiently without needing contiguous memory like arrays.
A linked list consists of nodes, where each node has two parts:
 - Data: The value stored in the node.
 - Next: A reference (or pointer) to the next node in the list.

 A singly linked list has nodes that each point to the next node.
 A doubly linked list has nodes that point to both the next node and the previous node, allowing traversal in both directions.

Summary of Linked List Methods:
 - append(data): Adds a new node with the given data to the end of the list.
 - insertAt(data, index): Inserts a new node with the given data at the specified index.
 - removeAt(index): Removes the node at the specified index.
 - print(): Prints the elements of the list in a readable format (e.g., 10 -> 15 -> 30).
 - getSize(): Returns the number of elements in the list.
 - isEmpty(): Checks if the list is empty.
 - find(data): Finds the node containing the specified data.
Time Complexity:
 - Append: O(n) – We may need to traverse the list to find the last node.
 - Insert at index: O(n) – We need to traverse the list to the specified index.
 - Remove at index: O(n) – We need to traverse to the specified index.
 - Find: O(n) – We may need to traverse the entire list to find a value.
*/

// 1. Create a Node Class
// A node has a data (value) and a next pointer to the next node.
class Node {
  constructor(data) {
    this.data = data; // The value of the node
    this.next = null; // The pointer to the next node (null by default)
  }
}

// 2. Create a LinkedList Class
// The linked list class will have methods to manipulate the list such as adding elements, removing elements, and displaying the list.
class LinkedList {
  constructor() {
    this.head = null; // The head points to the first node in the list
    this.size = 0; // Size to keep track of the number of elements
  }

  // Add a new node at the end of the list
  append(data) {
    const newNode = new Node(data);

    if (this.head === null) {
      // If the list is empty, make the new node the head
      this.head = newNode;
    } else {
      let current = this.head;

      // Traverse the list to find the last node
      while (current.next) {
        current = current.next;
      }

      // Make the last node's next point to the new node
      current.next = newNode;
    }

    this.size++;
  }

  // Insert a node at a specific position
  insertAt(data, index) {
    if (index < 0 || index > this.size) {
      return; // Index out of bounds
    }

    const newNode = new Node(data);

    if (index === 0) {
      // If inserting at the beginning, update head
      newNode.next = this.head;
      this.head = newNode;
    } else {
      let current = this.head;
      let previous;

      // Traverse to the desired index
      for (let i = 0; i < index; i++) {
        previous = current;
        current = current.next;
      }

      // Insert the new node
      newNode.next = current;
      previous.next = newNode;
    }

    this.size++;
  }

  // Remove the node at a specific index
  removeAt(index) {
    if (index < 0 || index >= this.size) {
      return; // Index out of bounds
    }

    let current = this.head;

    if (index === 0) {
      // Remove the head
      this.head = current.next;
    } else {
      let previous;
      for (let i = 0; i < index; i++) {
        previous = current;
        current = current.next;
      }

      // Skip the node to remove it
      previous.next = current.next;
    }

    this.size--;
  }

  // Print the list for easy debugging
  print() {
    let current = this.head;
    let result = [];
    while (current) {
      result.push(current.data);
      current = current.next;
    }
    console.log(result.join(" -> "));
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


const list = new LinkedList();
list.append(10);
list.append(20);
list.append(30);

console.log("Size of list:", list.getSize()); // Size of list: 3
list.print(); // 10 -> 20 -> 30

list.insertAt(15, 1); // Insert 15 at index 1
list.print(); // 10 -> 15 -> 20 -> 30

list.removeAt(2); // Remove element at index 2 (which is 20)
list.print(); // 10 -> 15 -> 30

console.log("Finding 15:", list.find(15)); // Node { data: 15, next: Node { data: 30, next: null } }
console.log("Finding 100:", list.find(100)); // null
