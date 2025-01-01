#------------------------------- QUICK SORT ALGORITHM ---------------------------------#
# Quick Sort is another divide - and - conquer algorithm.
# It works by selecting a pivot element from the array and partitioning the other elements into two subarrays—those less than the pivot and those greater than the pivot.
# These subarrays are then sorted recursively.


# Time Complexity:
#   - Best case: O(n log n) — Occurs when the pivot divides the array into roughly equal halves.
#   - Average case: O(n log n) — Most typical cases where the pivot performs well.
#   - Worst case: O(n²) — Occurs when the pivot is always the smallest or largest element (e.g., when the array is already sorted or nearly sorted).
# Space Complexity:
#   - O(log n) for the recursive stack in the best and average cases.
#   - O(n) in the worst case for the recursion stack.

# Summary:
# - Quick Sort is generally faster than other O(n log n) algorithms (like Merge Sort) in practice due to smaller constant factors and better cache performance.
# - The worst-case time complexity of O(n²) can be avoided with random pivot selection or using techniques like median-of-three to choose the pivot.
#-----------------------------------------------------------------------------------#

#-------------- Basic Example (Not in Place) ---------#
#-----------------------------------------------------#
def quick_sort(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a pivot (in this case, the last element)
    pivot = arr[-1]

    # Step 2: Partition the array into two subarrays
    left = [x for x in arr[:-1] if x <= pivot]  # Elements <= pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements > pivot

    # Step 3: Recursively sort the left and right subarrays, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
print("---------------------")


#----------------------------------- Quick Sort (In-place with Lomuto Partition Scheme) -------------------------------------#
# This is an in-place Quick Sort implementation using Lomuto’s partition scheme. 
# - It avoids the extra space used for creating new subarrays by partitioning the array directly. 
# - While Quick Sort is very efficient in practice (on average, O(n log n)), it can degrade to O(n²) in the worst case if the pivot selection is poor. 
# - To mitigate this, variations like randomized Quick Sort or median-of-three pivot selection can be used.
#------------------------------------------------------------------------#
def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Step 1: Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Step 2: Recursively sort the left and right subarrays
        quick_sort_in_place(arr, low, pivot_index - 1)  # Left subarray
        quick_sort_in_place(arr, pivot_index + 1, high) # Right subarray

# Lomuto's partition scheme
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:  # If current element is less than the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in its correct position
    return i + 1


arr_lomuto = [38, 27, 43, 3, 9, 82, 10]
print("(Initial) Array / List")
quick_sort_in_place(arr_lomuto)
print("Sorted array (Lomuto In place): ", arr_lomuto)
print("------------------------")


#------------------------------ Quick Sort Algorithm Using Hoare's Partition Scheme -------------------#
# Note - this scheme still Sorts In Place.
# - In Hoare's partition scheme, we select a pivot element (typically the first element),
# - and partition the array by moving two pointers toward each other—one from the left looking for an element greater than the pivot and one from the right looking for an element smaller than the pivot. 
# - These two elements are swapped.
# - This continues until the pointers cross, at which point the pivot is placed in its correct position.

# Time Complexity:
#   - Best case: O(n log n) — This occurs when the pivot divides the array into nearly equal parts.
#   - Average case: O(n log n) — Most common case when the pivot divides the array reasonably well.
#   - Worst case: O(n²) — This occurs when the pivot is always the smallest or largest element (e.g., if the array is already sorted or nearly sorted).
# Space Complexity:
#   - O(log n) for the recursion stack in the best and average cases (logarithmic depth of recursion).
#   - O(n) for the recursion stack in the worst case (if the array is already sorted or nearly sorted).
#
# Why Hoare's Partition Scheme is Better:
#   - Fewer swaps: Hoare's partitioning scheme typically requires fewer swaps than Lomuto's partition scheme, as it only performs a swap when the pointers i and j are out of order.
#   - More efficient: Since the pointers move towards each other from both ends, fewer elements need to be moved around, making the partitioning process more efficient.
# This version of Quick Sort is often faster in practice, especially for large arrays, due to fewer swaps and a more efficient partitioning process.
#-------------------------------------------------------------------------------------------#
def quick_sort_hoare(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Step 1: Partition the array and get the pivot index
        pivot_index = hoare_partition_scheme(arr, low, high)

        # Step 2: Recursively sort the left and right subarrays
        quick_sort_hoare(arr, low, pivot_index)  # Left subarray (including pivot)
        quick_sort_hoare(arr, pivot_index + 1, high)  # Right subarray (excluding pivot)


def hoare_partition_scheme(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot
    i = low - 1
    j = high + 1

    while True:
        # Move `i` to the right, looking for an element greater than the pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move `j` to the left, looking for an element smaller than the pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If the pointers have crossed, return the partition index
        if i >= j:
            return j

        # Swap elements at `i` and `j`
        arr[i], arr[j] = arr[j], arr[i]


arr_hoare = [38, 27, 43, 3, 9, 82, 10]
print("(Initial) Array", arr_hoare)
quick_sort_hoare(arr_hoare)
print("Sorted array (Hoares Partition Scheme) In place:", arr_hoare)
print("------------------------")
