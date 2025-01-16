# # Queue (FIFO) - Last in First Out

# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.next = None

# class Queue:
#   def __init__(self):
#     self.head = None
#     self.rear = None
#     self.size = 0

#   def is_empty(self):
#     return self.size == 0

#   def enqueue(self, value):
#     node = Node(value)
#     if self.is_empty():
#       # If the queue is empty, both front and rear will point to the new node
#       self.head = node
#       self.rear = node
#     else:
#       # Add the new node to the end of the queue (rear)
#       self.rear.next = node
#       self.rear = node
#     self.size += 1

#   def dequeue(self):
#     if self.is_empty():
#       return "Queue is Empty."
#     front_node = self.head.value # get value of head node
#     self.head = self.head.next # dequeue it and set head to the next node
#     if self.head is None: # If the queue becomes empty, set rear to None as well
#       self.rear = None
#     self.size -= 1 # decrement the queue size
#     return front_node

#   def peek(self):
#     if self.is_empty():
#       return "Queue is Empty"
#     return self.head.value

#   def get_size(self):
#     return self.size

#   def clear(self):
#     self.head = None
#     self.rear = None
#     self.size = 0

#   def print(self):
#     if self.is_empty():
#       return "Queue is Empty."
#     current = self.head
#     result = ""
#     while current is not None:
#       result += str(current.value) + " -> "
#       current = current.next
#     print(result)

# queue = Queue()

# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)

# queue.print() # 10 -> 20 -> 30 -> 40 ->

# queue.dequeue() # returns 10
# queue.print() # 20 -> 30 -> 40 ->

# print(queue.peek()) # 20
# print(queue.is_empty()) # False
# print(queue.get_size()) # 3

# queue.clear()
# print(queue.is_empty()) # True
# print("------------------------")

#------------------------------------------------#
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#------------------------------------------------#


'''
 Seven different symbols represent Roman numerals with the following values:

 Symbol	Value
  I	      1
  V	      5
  X	      10
  L	      50
  C	      100
  D	      500
  M	      1000

 Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.
 Converting a decimal place value into a Roman numeral has the following rules:
 - If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
 - If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
 - Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

 CHALLENGE:
 - Given an integer, convert it to a Roman numeral.
Example 1:

Input: num = 3749
Output: "MMMDCCXLIX"
Explanation:
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
'''

# def int_to_roman(num):
#     value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#     roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
#     ans = ""
#     for i in range(13):
#       while num >= value[i]:
#         ans = ans + roman[i]
#         num = num - value[i]
#     return ans

# print(int_to_roman(3749))


#############################################################
# H INDEX
#
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# - According to the definition of h-index on Wikipedia:
#   - The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
#
# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1
#############################################################

def h_index(citations):
  citations.sort()
  h_ind = 0
  for i in citations:
    if i <= len(citations) - i:
      h_ind = max(h_ind, citations[i])
    else:
      h_ind = max(h_ind, len(citations) - i)
  return h_ind


print(h_index([3,0,6,1,5]))
print(h_index([1,3,1]))
