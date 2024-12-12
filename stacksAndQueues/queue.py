# Queue (FIFO) - Last in First Out

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
