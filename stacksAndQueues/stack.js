//------------------------------------------------------------//
// Stack => LIFO
// Basic Stack Data Structure using an Array to hold items in the stack.
/*
Explanation:
 - add(element): Adds an element to the end of the array, simulating the "push" operation.
 - pop(): Removes and returns the last element of the array, simulating the "pop" operation. If the stack is empty, it returns null.
 - peek(): Returns the last element without removing it, simulating the "peek" operation.
 - isEmpty(): Returns true if the stack has no elements, otherwise false.
 - size(): Returns the number of elements in the stack.
 - clear(): Clears all elements from the stack.
*/
//------------------------------------------------------------//


class Stack {
  constructor() {
    this.items = [];
  }

  add(element) {
    this.items.push(element);
  }

  pop() {
    if (this.isEmpty()) {
      console.log("stack is empty");
      return null;
    }
    return this.items.pop();
  }

  peek() {
    if (this.isEmpty()) {
      console.log("stack is empty");
      return null;
    }
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length == 0;
  }

  size() {
    return this.items.length;
  }

  clear() {
    return (this.items = []);
  }
}

const stack = new Stack();
stack.add(10);
stack.add(20);
stack.add(30);
console.log(stack.peek()); // 30
console.log(stack.pop()); // 30
console.log(stack.size()); // 2
stack.clear();
console.log(stack.isEmpty()); // true
console.log(stack.peek()); // stack is empty
console.log("----------------------------");




//------------------------------------------------------------//
/*
Another way to implement a stack in JavaScript using a class would be to use a different data structure for storing the stack elements.
For instance, we can use an object to simulate the stack, where the keys represent the indices, and the values represent the stack elements.

Using an object:
- Here, the stack elements are stored in an object (this.items), where the keys are numeric indices, and the values are the elements of the stack.
- Count tracking: Instead of using length (which is used in arrays), we track the number of items in the stack with a count property.

- push(element): Adds the element to the object using the current count as the key, then increments the count.
- pop(): Decrements the count, retrieves the element at the new index (count - 1), and deletes the property from the object.
- peek(): Returns the value at this.items[count - 1].
- isEmpty(): Checks if count is 0.
- size(): Returns the value of count.
- clear(): Resets both items and count.

DIFFERENCES:
 - Array vs Object: This implementation uses an object to store elements instead of an array.
     - This can be useful in cases where you want to avoid using array-specific methods like push() and pop() directly.
 - Tracking Size: The stack size is explicitly managed with the count property, rather than relying on the array's length.
 - Memory Considerations: While an array will automatically resize, using an object may offer slightly better performance in some cases (though this is mostly for large datasets).
*/

// This approach gives a more low-level handling of the stack, providing more control over the stack behavior in some scenarios.
//------------------------------------------------------------//


class Stack_2 {
  constructor() {
      this.items = {}; // Object to hold stack items
      this.count = 0; // Tracks the number of elements in the stack
  }

  add(element) {
      this.items[this.count] = element;
      this.count++;
  }

  pop() {
      if (this.isEmpty()) {
          console.log("Stack is empty");
          return null;
      }

      this.count--;
      const result = this.items[this.count];
      delete this.items[this.count]; // Remove the element from the object
      return result;
  }

  peek() {
      if (this.isEmpty()) {
          console.log("Stack is empty");
          return null;
      }
      return this.items[this.count - 1];
  }

  isEmpty() {
      return this.count === 0;
  }

  size() {
      return this.count;
  }

  clear() {
      this.items = {};
      this.count = 0;
  }
}


const stack2 = new Stack_2();
stack2.add(10);
stack2.add(20);
stack2.add(30);
console.log(stack2.peek()); // 30
console.log(stack2.pop());  // 30
console.log(stack2.size()); // 2
stack2.clear();
console.log(stack2.isEmpty()); // true
console.log(stack2.peek()); "Stack is empty"
console.log("----------------------------");
