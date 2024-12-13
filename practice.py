"""
Given a sorted array of numbers, determine if a number exists.

Input : sorted = [0, 1, 1, 2, 5, 7, 9, 9, 10], find if these exist [5, 3, 8, 7]
Output: [y, n, n, y]

[0, 1, 1, 2, 5, 7, 9, 9, 10], 5
min = 0, max = 8, guess = 4
nums[4] = 5 == 5 --> y

[0, 1, 1, 2, 5, 7, 9, 9, 10], 3
min = 0, max = 8, guess = 4
nums[4] = 5 == 3 --> ??
"""




def doBinarySearch(sorted_list, search_list):
    results = []
    for target in search_list:
      # if target not in sorted_list:
      #   results.append("n")
      # else:
        min = 0
        max = len(sorted_list) - 1
        while min <= max:
          middle = (min + max) // 2
          if sorted_list[middle] == target:
            results.append("y")
          if sorted_list[middle] < target:
            min = middle + 1
          if sorted_list[middle] > target:
            max = middle - 1

        results.append("n")

    return results


#print(doBinarySearch([0, 1, 1, 2, 5, 7, 9, 9, 10], [5, 3, 8, 7]))
print("--------------")
