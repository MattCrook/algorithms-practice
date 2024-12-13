#----------------------------------------------#
# Search the List of prime numbers for a given value using a binary search
#-----------------------------------------------#
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

class DoBinarySearch(object):
  def do_search(self, input_list, target):
    min = 0
    max = len(input_list) - 1
    guess = 0
    while min <= max:
      guess = math.floor((min + max) // 2)
      if input_list[guess] == target:
        return guess
      elif input_list[guess] < target:
        min = guess + 1
      elif input_list[guess] > target:
        max = guess - 1
    return -1

solution_1 = DoBinarySearch()
print("solution_1", solution_1.do_search(primes, 73)) # 20
print("--------------------------")




class DoBinarySearchRecursion(object):
  def do_search_recursion(self, input_list, target, min, max):
    if min > max:
      return -1
    # finding middle of list by getting average.
    middle = math.floor((min + max) // 2)

   # if it equals, it is successful so return it.
    if input_list[middle] == target:
      return middle

    # if middle is greater than target, we don't need everything above that number
    # so set new max to middle -1 (b/c doesn't equal current number either.)
    if input_list[middle] > target:
      return self.do_search_recursion(input_list, target, min, (middle - 1))

    # if middle less than target, we don't need anything below that number.
    # so set new min to middle + 1 (b/c doesn't equal current number either.)
    if input_list[middle] < target:
      return self.do_search_recursion(input_list, target, (middle + 1), max)


solution_2 = DoBinarySearchRecursion()
print("solution_2", solution_2.do_search_recursion(primes, 73, 0, len(primes) - 1)) # 20
print("solution_2", solution_2.do_search_recursion(primes, 79, 0, len(primes) - 1)) # 20
print("--------------------------")



# Put it all together in one Class
class BinarySearch(object):
  def binarySearch(self, input_list, target):
    min = 0
    max = len(input_list) - 1
    guess = 0
    while min <= max:
      guess = math.floor((min + max) // 2)
      if input_list[guess] == target:
        return guess
      if input_list[guess] < target:
        min = guess + 1
      elif input_list[guess] > target:
        max = guess - 1
    return -1

  def binarySearchRecursion(self, input_list, target, min, max):
    if min > max:
      return -1
    guess = math.floor((min + max) // 2)
    if input_list[guess] == target:
      return guess
    if input_list[guess] < target:
      return self.binarySearchRecursion(input_list, target, guess + 1, max)
    if input_list[guess] > target:
      return self.binarySearchRecursion(input_list, target, min, guess - 1)



binarySearch = BinarySearch()
print("binarySearchClass", binarySearch.binarySearch(primes, 7))
print("binarySearchClass", binarySearch.binarySearchRecursion(primes, 7, 0, len(primes) - 1))
print("--------------------------")
