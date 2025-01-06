####################################################################
# Given a sorted array of numbers, determine if a number exists.
#
# Input : sorted = [0, 1, 1, 2, 5, 7, 9, 9, 10], find if these exist [5, 3, 8, 7]
# Output: [y, n, n, y]
####################################################################


#---------------- SOLUTION 01 -----------------------#
# Input:
# - A sorted array of numbers ("sorted_array").
# - A list of numbers (target_list) that we want to check against the "sorted_array".
# Output:
# - For each number in target_list, return "y" if it exists in "sorted_array", otherwise return "n".
# Approach:
# - For each number in the target_list, perform a binary search on the "sorted_array" to check if it exists.
# - If any number is found, return "y", otherwise return "n".
#---------------------------------------#
class SearchListBinarySearch(object):

  def binary_search_helper(self, arr, target):
      """
      Helper function that will be called for each number in the
      search_list, and perform a binary search to see if in the sorted_list.
      """
      left, right = 0, len(arr) - 1

      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return True
          elif arr[mid] < target:
              left = mid + 1
          else:
              right = mid - 1

      return False


  def checkElementsInSortedList(self, sorted_list, search_list):
      """
      Returns a list/array of strings of "y" or n",
      of the results of if number is in list.
      Ex) ['y', 'n', 'n', 'y']
      binary_search function:

      - This function performs binary search on "sorted_array" to check if target exists.
      - It returns True if the number is found, otherwise False.
      - check_numbers_in_sorted_array function:

      - This function iterates through each element in the "target_list".
      - For each element, it calls binary_search to check if the number exists in the sorted_array.
      - It appends "y" if the number is found, or "n" if it's not found, to the results list.

      Time Complexity:
      - Binary Search: Each binary search takes O(log n) time, where n is the length of sorted_array.
      - Overall Complexity: If m is the length of target_list, and n is the length of sorted_array, the total time complexity is O(m * log n).
      """
      results = []

      for target in search_list:
          if self.binary_search_helper(sorted_list, target):
            results.append("y")
          else:
            results.append("n")

      return results


searchListBinarySearch = SearchListBinarySearch()
print(searchListBinarySearch.checkElementsInSortedList_02([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]))
print("----------------")


#---------------- SOLUTION 02 (Simpler Than 01) -----------------------#
# Just prints out "y" or "n" by calling the function.
#----------------------------------------------------------#
class SearchListBinarySearch_02(object):

  def binary_search_helper(self, arr, target):
      """
      Helper function that will be called for each number in the
      search_list, and perform a binary search to see if in the sorted_list.
      """
      left, right = 0, len(arr) - 1

      while left <= right:
          mid = (left + right) // 2
          if arr[mid] == target:
              return True  # The number exists in the array
          elif arr[mid] < target:
              left = mid + 1  # Search the right half
          else:
              right = mid - 1  # Search the left half

      return False  # The number does not exist in the array

  def checkElementsInSortedList(self, sorted_list, search_list):
      """
      Simple solution just prints out strings of "y" or n".
      Of the results of if number is in list.
      Ex)
         y
         n
         n
         y
      """
      for target in search_list:
          if self.binary_search_helper(sorted_list, target):
            print("y")
          else:
            print("n")


searchListBinarySearch_02 = SearchListBinarySearch_02()
searchListBinarySearch_02.checkElementsInSortedList_02([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7])
print("----------------")



#-------------------- SOLUTION 03 -------------------#
# Solution combining what was the helper function and "main" function
# in the previous examples.
#
# The function checks each number from the target_list against the sorted_array using binary search.
# It efficiently returns "y" for found numbers and "n" for missing numbers.
#--------------------------------------------#
def check_numbers_in_sorted_array(sorted_array, target_list):
    def do_binary_search(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    results = []
    for target in target_list:
        results.append("y" if do_binary_search(sorted_array, target) else "n")

    return results

print(check_numbers_in_sorted_array([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]))
print("--------------")


#-------------------- SOLUTION 04: RECURSION -------------------#
# Using method of Solution #3 of combining into (1) Function.
# But solving Binary Search using a recursive function.
#----------------------------------------------------#
def check_numbers_in_sorted_array_recursion(sorted_array, target_list):
    def do_binary_search_rec(arr, target, minn, maxx):
        if minn > maxx:
            return False
        mid = (minn + maxx) // 2
        if (mid == target):
            return True
        if arr[mid] < target:
            return do_binary_search_rec(arr, target, mid + 1, maxx)
        else:
            return do_binary_search_rec(arr, target, minn, mid - 1)

    results = []
    for target in target_list:
        results.append("Y" if do_binary_search_rec(sorted_array, target, 0, len(sorted_array) - 1) else "N")

    return results

print(check_numbers_in_sorted_array_recursion([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]))
print("--------------")
