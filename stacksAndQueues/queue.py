# Queue (FIFO) - Last in First Out


# --------------- SOLUTION #1 ---------- #
# Simple implementation of a queue using a List.
# ----------------------------------------- #
class Queue:
  def __init__(self):
    self.items = []

  def add(self, item):
    self.items.append(item)

  def remove(self):
    if self.isEmpty():
      print("queue is empty")
    self.items.remove(self.items[0])

  def isEmpty(self):
    return len(self.items) == 0

  def peek(self):
    if self.isEmpty():
      print("queue is empty")
    return self.items[0]

  def peek_whole_queue(self):
    if self.isEmpty():
      print("queue is empty")
    return self.items

  def size(self):
    return len(self.items)


queue = Queue()
queue.add(1)
queue.add(3)
print(queue.isEmpty()) # false
print(queue.peek()) # 1
queue.remove()
print(queue.peek()) # 3
queue.add(5)
print(queue.peek_whole_queue()) # [3, 5]
print(queue.size()) # 2
print('--------------------')


# ----------------- SOLUTION #2 ------------------- #
# Queue implementation using a linked list.
# - A linked list allows for more efficient enqueue and dequeue operations, as the enqueue operation (adding to the tail) and dequeue operation (removing from the head)
# - A linked-list-based queue is efficient, especially for queues where frequent enqueue and dequeue operations are needed.
# -------------------------------------------------- #
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.rear = None
    self.size = 0

  def is_empty(self):
    return self.size == 0

  def enqueue(self, value):
    node = Node(value)
    if self.is_empty():
      # If the queue is empty, both front and rear will point to the new node
      self.head = node
      self.rear = node
    else:
      # Add the new node to the end of the queue (rear)
      self.rear.next = node
      self.rear = node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      return "Queue is Empty."
    front_node = self.head.value # get value of head node
    self.head = self.head.next # dequeue it and set head to the next node
    if self.head is None: # If the queue becomes empty, set rear to None as well
      self.rear = None
    self.size -= 1 # decrement the queue size
    return front_node

  def peek(self):
    if self.is_empty():
      return "Queue is Empty"
    return self.head.value

  def get_size(self):
    return self.size

  def clear(self):
    self.head = None
    self.rear = None
    self.size = 0

  def print(self):
    if self.is_empty():
      return "Queue is Empty."
    current = self.head
    result = ""
    while current is not None:
      result += str(current.value) + " -> "
      current = current.next
    print(result)



queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.print() # 10 -> 20 -> 30 -> 40 ->

queue.dequeue() # returns 10
queue.print() # 20 -> 30 -> 40 ->

print(queue.peek()) # 20
print(queue.is_empty()) # False
print(queue.get_size()) # 3

queue.clear()
print(queue.is_empty()) # True
print("------------------------")
