#------------------------------- SELECTION SORT ALGORITHM ---------------------------------#
# Selection Sort is a simple comparison-based sorting algorithm that works by repeatedly finding the minimum (or maximum) element from the unsorted part of the list and swapping it with the first unsorted element. 
# It works by reducing the unsorted portion of the array step by step.
# - It uses in-place sorting, meaning the algorithm sorts the array in place without needing extra memory
# - it is non-stable meaning that it may change the relative order of equal elements
# - The algorithm always performs O(n²) comparisons, regardless of the input's order.
#------------------------------------------------------------------------------------------#

#--------- Sorting an Array in Ascending Order ---------#
# Suppose you have the following unsorted array: [64, 25, 12, 22, 11]

# Time Complexity:
#  - Best, Worst, and Average Case: O(n²), where n is the number of elements in the array.
#  - Space Complexity: O(1), since it only requires a constant amount of extra space for swaps.
#
# - First Pass (i = 0):
#  - Find the minimum element from the unsorted part: [64, 25, 12, 22, 11]
#  - The minimum element is 11.
#  - Swap 11 with the first element (64).
#
# - Second Pass (i = 1):
#  - Find the minimum element from the unsorted part: [25, 12, 22, 64]
#  - The minimum element is 12.
#  - Swap 12 with the second element (25).

# - Third Pass (i = 2):
#  - Find the minimum element from the unsorted part: [25, 22, 64]
#  - The minimum element is 22.

# - Fourth Pass (i = 3):
#  - Find the minimum element from the unsorted part: [25, 64]
#  - The minimum element is 25, which is already in place.
#  - No swap needed.

# - Fifth Pass (i = 4):
#  - The last element is already in its correct position.
#  - No further swaps needed.
#------------------------------------------------#
def selection_sort_simple(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort_simple(arr)
print("selection_sort_simple: ", sorted_arr)
print("-------------------")
