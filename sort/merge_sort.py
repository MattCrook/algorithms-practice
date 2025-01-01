#------------------------------- MERGE SORT ALGORITHM ---------------------------------#
# Merge Sort is a divide-and-conquer algorithm.
# It works by dividing the array into two halves, sorting each half recursively, and then merging the sorted halves.
#
# Steps:
#  - Divide the unsorted list into two halves.
#  - Recursively sort each half.
#  - Merge the two sorted halves to produce the final sorted list.

# Example Explanation:
# - merge_sort(arr) function:
#   - The list is divided into two halves recursively until each sublist has only one element.
# - merge(left, right) function:
#   - The function takes two sorted lists (left and right) and merges them into a single sorted list. It compares the elements from both lists and adds the smaller one to the sorted_list. After one of the lists is exhausted, it appends the remaining elements from the other list.
#
# Time Complexity:
#  - Best case: O(n log n)
#  - Average case: O(n log n)
#  - Worst case: O(n log n)
#-------------------------------------------------------------------------------------#

def merge_sort(arr):
    # Base case: if the list has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare the elements of left and right lists and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # If there are remaining elements in either left or right, add them to the result
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array: ", sorted_arr) # Output => Sorted array: [3, 9, 10, 27, 38, 43, 82]
