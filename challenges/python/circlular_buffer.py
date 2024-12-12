#########################################################
# Create an efficient circular buffer in python (with the goal of taking averages of the integer values in the buffer)

# FOR MOR SULUTIONS and DETAILS, SEE:
#  - https://github.com/MattCrook/algorithms-practice/circularBuffer

#########################################################


#------------------------------------------------------#
# SOLUTION 1 (More Simple Solution)
# Key Operations for a Circular Buffer:
#  - Write (Insert new data into the buffer).
#  - Read (Retrieve data from the buffer).
#  - Overwrite (When the buffer is full and new data comes in, the oldest data is overwritten).
#  - Check if Full (Determine if the buffer is full).
#  - Check if Empty (Determine if the buffer is empty).
#
# Explanation:
# - Constructor (__init__): Initializes the buffer size, a list to store elements, pointers (head, tail), and flags for checking if the buffer is full or empty.
# - write method: Adds data to the buffer. If the buffer is full, it overwrites the oldest data by moving the tail pointer.
# - read method: Retrieves data from the buffer. If the buffer is empty, it returns None.
# - is_full and is_empty methods: Check whether the buffer is full or empty.
# - __str__ method: Provides a string representation of the buffer’s current state for easier debugging.
# Buffer Behavior:
# - If the buffer is full and you write new data, it overwrites the oldest data.
# - If the buffer is empty and you try to read, it returns None.
#------------------------------------------------------#

class CircularBuffer:
    def __init__(self, size):
        self.size = size            # Size of the buffer
        self.buffer = [None] * size  # Buffer to store elements
        self.head = 0               # Points to the next position to write
        self.tail = 0               # Points to the next position to read
        self.full = False           # Flag to indicate if the buffer is full
        self.empty = True           # Flag to indicate if the buffer is empty

    def write(self, data):
        """Write data to the buffer. Overwrites oldest data if the buffer is full."""
        if self.full:
            # If buffer is full, move the tail pointer to the next element
            self.tail = (self.tail + 1) % self.size

        # Write the new data to the current head position
        self.buffer[self.head] = data

        # Move the head pointer to the next position
        self.head = (self.head + 1) % self.size

        # If head and tail point to the same position, buffer is full
        if self.head == self.tail:
            self.full = True
        else:
            self.full = False

        # If head equals tail, buffer is not empty
        self.empty = False

    def read(self):
        """Read data from the buffer. Returns None if buffer is empty."""
        if self.empty:
            return None

        # Read the data at the current tail position
        data = self.buffer[self.tail]

        # Move the tail pointer to the next position
        self.tail = (self.tail + 1) % self.size

        # If the tail has caught up with the head, buffer is empty
        if self.tail == self.head:
            self.empty = True
        self.full = False

        return data

    def is_full(self):
        """Returns True if the buffer is full."""
        return self.full

    def is_empty(self):
        """Returns True if the buffer is empty."""
        return self.empty

    def __str__(self):
        """Return a string representation of the buffer."""
        return f'Buffer: {self.buffer}, Head: {self.head}, Tail: {self.tail}, Full: {self.full}, Empty: {self.empty}'

# Example Usage
cb = CircularBuffer(5)

# Writing to the buffer
cb.write(10)
cb.write(20)
cb.write(30)
print(cb)  # Buffer: [10, 20, 30, None, None]

# Reading from the buffer
print(cb.read())  # 10
print(cb.read())  # 20

# Adding more data
cb.write(40)
cb.write(50)
cb.write(60)
print(cb)  # Buffer: [60, 20, 30, 40, 50]

# Overwriting the oldest data (10) after full buffer
cb.write(70)
print(cb)  # Buffer: [60, 70, 30, 40, 50]
print("--------------------------")



#-------------------------------------------------------------------------------#
# SOLUTION 2 (Additional Solution)
# From Github:
# - https://github.com/heineman/python-data-structures/blob/master/2.%20Ubiquitous%20Lists/circBuffer.py
#-------------------------------------------------------------------------------#
class CircularBuffer:

    def __init__(self, size):
        """Store buffer in given storage."""
        self.buffer = [None]*size
        self.low = 0
        self.high = 0
        self.size = size
        self.count = 0

    def isEmpty(self):
        """Determines if buffer is empty."""
        return self.count == 0

    def isFull(self):
        """Determines if buffer is full."""
        return self.count == self.size

    def __len__(self):
        """Returns number of elements in buffer."""
        return self.count

    def add(self, value):
        """Adds value to buffer, overwrite as needed."""
        if self.isFull():
            self.low = (self.low+1) % self.size # Modulus (returns the remainder of a division operation)
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size # Modulus (returns the remainder of a division operation)

    def remove(self):
        """Removes oldest value from non-empty buffer."""
        if self.count == 0:
            raise Exception ("Circular Buffer is empty");
        value = self.buffer[self.low]
        self.low = (self.low + 1) % self.size
        self.count -= 1
        return value

    def __iter__(self):
        """Return elements in the circular buffer in order using iterator."""
        idx = self.low
        num = self.count
        while num > 0:
            yield self.buffer[idx]
            idx = (idx + 1) % self.size
            num -= 1

    def __repr__(self):
        """String representation of circular buffer."""
        if self.isEmpty():
            return 'cb:[]'

        return 'cb:[' + ','.join(map(str,self)) + ']'

if __name__=='__main__':
    cb=CircularBuffer(5)
    cb.add(1); cb.add(2); cb.add(3); cb.add(4)
    print(cb.__repr__())
    cb.add(5)
    print(cb.__repr__())
    cb.add  (6)
    print(cb.__repr__())
    cb.add(7); cb.add(8); cb.add(9); cb.add(10)
    print(cb.__repr__())
    print("_len__:", cb.__len__())
print("--------------------------")
