#########################################################
# Create an efficient circular buffer in python (with the goal of taking averages of the integer values in the buffer)
#########################################################

# it's the nice batteries included way....use collections.deque with a maxlen arg
# https://docs.python.org/3/library/collections.html#deque-recipes
# import collections
# d = collections.deque(maxlen=10)
# d
# deque([], maxlen=10)
# for i in xrange(20):
#   d.append(i)
# deque([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], maxlen=10)

#------------------------------------------------#
# Solution from the Python Cookbook, including a reclassification of the ring buffer instance when it becomes full
# - The notable design choice in the implementation is that, since these objects undergo a nonreversible state transition at some point in their lifetimes—from non-full buffer to full-buffer (and behavior changes at that point) —I modeled that by changing self.__class__. 
# This works even in Python 2.2, as long as both classes have the same slots (for example, it works fine for two classic classes, such as RingBuffer and __Full in this recipe).
#------------------------------------------------#
class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self,size_max):
        self.max = size_max
        self.data = []

    class __Full:
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x
            self.cur = (self.cur+1) % self.max
        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print(x.__class__, x.get())
    x.append(5)
    print(x.__class__, x.get())
    x.append(6)
    print(x.data, x.get())
    x.append(7); x.append(8); x.append(9); x.append(10)
    print(x.data, x.get())
print("--------------------------")



#-------------------------------------------------------------------------------#
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
            self.low = (self.low+1) % self.size
        else:
            self.count += 1
        self.buffer[self.high] = value
        self.high = (self.high + 1) % self.size

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

#------------------------------------------------#
# Another possible solution.
#------------------------------------------------#

# import numpy
# import timeit
# import collections

# class CircularBuffer(object):
#     buffer_methods = ('list', 'deque', 'roll')

#     def __init__(self, buffer_size, buffer_method):
#         self.content = None
#         self.size = buffer_size
#         self.method = buffer_method
#         self.update = getattr(self, '_update_' + buffer_method)

#     def _update_list(self, scalar):
#         try:
#             # shift
#             self.content.append(scalar)
#             self.content.pop(0)
#         except AttributeError:
#             # init
#             self.content = [0.] * self.size

#     def _update_deque(self, scalar):
#         try:
#             # shift
#             self.content.append(scalar)
#         except AttributeError:
#             # init
#             self.content = collections.deque([0.] * self.size, maxlen=self.size)

#     def _update_roll(self, scalar):
#         try:
#             # shift
#             self.content = numpy.roll(self.content, -1)
#             self.content[-1] = scalar
#         except IndexError:
#             # init
#             self.content = numpy.zeros(self.size, dtype=float)


# # Testing and Timing
# circular_buffer_size = 100
# circular_buffers = [
#     CircularBuffer(buffer_size=circular_buffer_size, buffer_method=method)
#     for method in CircularBuffer.buffer_methods
# ]
# timeit_iterations = 1e4
# timeit_setup = 'from __main__ import circular_buffers'
# timeit_results = []
# for i, cb in enumerate(circular_buffers):
#     # We add a convenient number of convenient values (see equality test below)
#     code = '[circular_buffers[{}].update(float(j)) for j in range({})]'.format(
#         i, circular_buffer_size
#     )
#     # Testing
#     eval(code)
#     buffer_content = [item for item in cb.content]
#     assert buffer_content == list(range(circular_buffer_size))
#     # Timing
#     timeit_results.append(
#         timeit.timeit(code, setup=timeit_setup, number=int(timeit_iterations))
#     )
#     print(
#         '{}: total {:.2f}s ({:.2f}ms per iteration)'.format(
#             cb.method,
#             timeit_results[-1],
#             timeit_results[-1] / timeit_iterations * 1e3,
#         )
#     )
