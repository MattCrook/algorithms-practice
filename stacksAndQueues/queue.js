// --------- A Queue implements FIFO (first-in, first-out) ordering. ----------//

//---------------------------------------------------------------------//
/*
SOLUTION #1

Simple implementation of a queue using an array.
This version includes basic queue operations like:
  - add (enqueue) (adding an element)
  - remove (dequeue) (removing an element)
  - peek (viewing the front element without removing it)
  - isEmpty(): Checks if the queue is empty.
  - size(): Returns the number of elements in the queue.
  - clear(): Clears all elements from the queue.
  - print(): Displays the elements in the queue for easy visualization.

This is a simple implementation.
In a more performance-critical scenario, you could use a linked list or a more advanced data structure to avoid performance bottlenecks when dealing with large queues.
*/
//---------------------------------------------------------------------//
class Queue {
  constructor() {
    this.items = [];
  }

  // Adds an element to the end of the queue
  add(item) {
    this.items.push(item);
  }

  // Removes specific item of the queue
  // (not really a queue thing, but here just for fun)
  removeItem(item) {
    if (this.isEmpty()) {
      console.log("Queue is empty");
    } else {
      const index = this.items.indexOf(item);
      this.items.splice(index, item);
      console.log(`removed ${item} from index ${index} in queue.`);
      return this.print();
    }
  }

  // Removes and returns the front element of the queue
  remove() {
    if (this.isEmpty()) {
      console.log("Queue is empty");
    } else {
      return this.items.shift();
    }
  }

  // Boolean check, returns true if the queue is empty
  isEmpty() {
    return this.items.length == 0;
  }

  // Returns the front element without removing it
  peek() {
    if (this.isEmpty()) {
      console.log("Queue is empty");
    } else {
      return this.items[0];
    }
  }

  // Returns whole queue.
  peekEntireQueue() {
    if (this.isEmpty()) {
      console.log("Queue is empty");
    } else {
      return this.items;
    }
  }

  // Returns the number of elements in the queue
  size() {
    return this.items.length;
  }

  // console.logs all items separated by "<-"
  print() {
    console.log(this.items.join(" <- "));
  }

  // Clears the queue
  clear() {
    this.items = [];
  }
}

// ----- Example usage: -----//
const queue = new Queue();
const numbersToAdd = [10, 20, 30, 50, 100];

// Function to add numbers
function addNumbersToQueue(numbers, q) {
  numbers.forEach((number) => q.add(number));
}

addNumbersToQueue(numbersToAdd, queue);

// adding numbers manually
// queue.add(10);
// queue.add(20);
// queue.add(30);
// queue.add(50);
// queue.add(100);

queue.print(); // 10 <- 20 <- 30 <- 50 <- 100

console.log(queue.remove()); // 10
queue.print(); // 20 <- 30 <- 50 <- 100

console.log(queue.peek()); // 20
console.log(queue.isEmpty()); // false
console.log(queue.size()); // 4

queue.removeItem(50); // removed 50 from index 2 in queue.
// 20 <- 30

queue.clear();
console.log(queue.isEmpty()); // true
console.log("------------------------");

//---------------------------------------------------------------------//
/*
SOLUTION #2

Queue implementation using a linked list.
A linked list allows for more efficient enqueue and dequeue operations, as the enqueue operation (adding to the tail) and dequeue operation (removing from the head)
Both take constant time 𝑂(1) O(1), unlike with arrays where shift() or unshift() can be slow due to re-indexing.

Node class:
- A simple class for the nodes of the linked list.
- Each node stores a value and has a pointer (next) to the next node.

Queue class:
 - enqueue(value): Creates a new node and adds it to the end (rear) of the queue.
 - dequeue(): Removes and returns the value of the node at the front of the queue. If the queue is empty, it returns an error message.
 - peek(): Returns the value of the front node without removing it from the queue.
 - isEmpty(): Checks if the queue is empty by checking if size is 0.
 - getSize(): Returns the current number of elements in the queue.
 - clear(): Resets the queue by setting front and rear to null and size to 0.
 - print(): Prints the queue elements from front to rear in a readable format.

Efficiency:
- Both enqueue and dequeue operations are O(1) since we're only updating pointers, not shifting elements.
- Dynamic Size: The queue grows and shrinks dynamically as we add and remove elements.
- Memory: Each node in the linked list uses memory for the value and next pointer, so there’s slightly more overhead compared to an array-based queue.

This linked-list-based queue is efficient, especially for queues where frequent enqueue and dequeue operations are needed.
*/
//---------------------------------------------------------------------//

class Node {
  constructor(value) {
    this.value = value; // Data to store
    this.next = null; // Pointer to the next node
  }
}

class QueueLinkedList {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0; // Number of elements in the queue
  }

  // Adds an element to the end of the queue
  enqueue(value) {
    const newNode = new Node(value);

    // If the queue is empty, both front and rear point to the new node
    if (this.isEmpty()) {
      this.front = newNode;
      this.rear = newNode;
    } else {
      this.rear.next = newNode; // Link the current rear node to the new node
      this.rear = newNode; // Move the rear pointer to the new node
    }
    this.size++;
  }

  // Removes and returns the front element of the queue
  dequeue() {
    if (this.isEmpty()) {
      return "Queue is empty";
    } else {
      const frontNode = this.front.value; // Get the value of the front node (dequeued node)
      this.front = this.front.next; // move the pointer to the next node

      // If the queue becomes empty, rear should also be null
      if (this.front === null) {
        this.rear = null;
      }

      // Decrement the size of the queue
      this.size--;
      return frontNode;
    }
  }

  peek() {
    if (this.isEmpty()) {
      return "Queue is empty";
    } else {
      return this.front.value;
    }
  }

  // Returns the total number of elements in the queue.
  getSize() {
    return this.size;
  }

  // Clears the entire queue
  clear() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  // Prints the elements in the queue (for visualization)
  print() {
    if (this.isEmpty()) {
      console.log("Queue is empty");
      return;
    }
    let current = this.front;
    let result = "";
    while (current != null) {
      result += current.value + " -> ";
      current = current.next;
    }

    // Remove the trailing " -> "
    // console.log(result.slice(0, -4)) // manually do it (not practical)
    const lastIndexOfTrailingArrow = result.lastIndexOf(" -> "); // Get the index of the last occurrence of " -> "
    const resultLessTrailingArrow = result.slice(0, lastIndexOfTrailingArrow); // slice the result by that value
    console.log(resultLessTrailingArrow);

    // console.log(this.removeTrailingArrow(result, " -> ")); // Use of helper function to abstract logic.
  }

  // Boolean check, returns true if the queue is empty
  isEmpty() {
    return this.size === 0;
  }

  // Helper - (edge case element not found)
  // Finds the index of the last occurrence of the specified element in the array.
  // If the element isn't found, it returns -1.
  removeTrailingArrow(arr, element) {
    const lastIndex = arr.lastIndexOf(element);
    if (lastIndex != -1) {
      arr.slice(0, lastIndex);
    }
    return arr;
  }
}

// ----- Example usage: -----//
const queueLinkedList = new QueueLinkedList();

queueLinkedList.enqueue(10);
queueLinkedList.enqueue(20);
queueLinkedList.enqueue(30);

queueLinkedList.print(); // 10 -> 20 -> 30

console.log(queueLinkedList.dequeue()); // 10
queueLinkedList.print(); // 20 -> 30

console.log(queueLinkedList.peek()); // 20
console.log(queueLinkedList.isEmpty()); // false
console.log(queueLinkedList.getSize()); // 2

queueLinkedList.clear();
console.log(queueLinkedList.isEmpty()); // true
console.log("------------------------");
