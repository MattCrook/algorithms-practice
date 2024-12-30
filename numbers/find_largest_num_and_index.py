#----------------------------------------------------#
# Find the largest number in the array and return the number AND its index.
#
# Showing multiple solutions below. More than one way to solve this.

numbers = [10, 7, 5, 8, 11, 9];
#----------------------------------------------------#


#--------------- SOLUTION 01 -------------------#
def solution_01(arr):
  sol = {}
  largest_num = max(arr)
  for n in range(0, len(arr)):
    index = n
    value = arr[n]
    if value == largest_num:
      sol["value"] = value
      sol["index"] = index
  return sol

print(solution_01(numbers))
print("--------------")


#--------------- SOLUTION 02 -------------------#
def solution_02(arr):
  largest = numbers[0]  # Assume the first number is the largest initially
  for number in arr:
      if number > largest:
          largest = number
  return {"index": arr.index(largest), "value": largest}

print(solution_02(numbers))
print("-------")


def return_just_largest(arr):
  largest = numbers[0]
  for number in arr:
      if number > largest:
          largest = number
  return largest

largest = solution_02(numbers)
print("Largest number is: ", largest)
print("--------------")


#--------------- SOLUTION 03 -------------------#
def solution_03(arr):
  largest = numbers[0]
  index_of_largest = 0
  for i in range(1, len(arr)):
      if numbers[i] > largest:
          largest = numbers[i]
          index_of_largest = i
  return {"largest": largest, "index": index_of_largest}

print(solution_03(numbers))
print("--------------")


#--------------- SOLUTION 04 -------------------#
def solution_04(arr):
  largest = max(arr)
  for i, num in enumerate(arr):
    if num == largest:
      return {"index": i, "value": num}

print(solution_04(numbers))
