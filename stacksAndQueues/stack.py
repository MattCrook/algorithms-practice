#----------------------------------------#
# Stack (LIFO - last in first out)
# SUPER Basic Stack Data Structure using an Array to hold items in the stack.

# Explanation:
#  - add(element): Adds an element to the end of the array, simulating the "push" operation.
#  - remove(): Removes and returns the last element of the array, simulating the "pop" operation. If the stack is empty, it returns null.
#  - peek(): Returns the last element without removing it, simulating the "peek" operation.
#  - isEmpty(): Returns true if the stack has no elements, otherwise false.
#  - size(): Returns the number of elements in the stack.
#  - clear(): Clears all elements from the stack.
#----------------------------------------#
class Stack:
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items.append(item)

  def remove(self):
    if self.isEmpty():
      print("stack is empty")
    self.items.pop()

  def isEmpty(self):
    return len(self.items) == 0

  def size(self):
    return len(self.items)

  def clear(self):
    self.items = []

  def peek(self):
    if self.isEmpty():
      print("stack is empty")
    return self.items[len(self.items) - 1]


stack = Stack()
stack.add(1)
stack.add(3)
stack.add(5)
print(stack.size()) # 3
print(stack.peek()) # 5
stack.remove()
print(stack.peek()) # 3
stack.clear()
print(stack.size()) # 0
print(stack.isEmpty()) # True
print("-----------------")
