'''
SUMMARY

Time Complexity

- Time complexity is concerned with how the running time of an algorithm or function grows as the size of the input increases. 
- We analyze the time complexity by counting the number of basic operations or steps the function performs, and then express that in Big-O notation.

Steps to analyze time complexity:
- Identify the Input Size:
  - The input size n is usually the number of elements that the algorithm operates on. For example, for a list of numbers, n is the number of elements in the list.
  - Break the function into parts:
    - For loops, recursive calls, function calls, etc., all contribute to the overall time complexity. You need to carefully examine how many times these parts are executed.

- Determine dominant terms:
  - In most cases, you focus on the term with the highest growth rate. For instance:
    - A single loop over n elements results in O(n).
    - A nested loop over n elements results in O(n²).
    - A recursive function with halving input size results in O(log n).

- Simplify to Big-O notation:
  - The Big-O notation is used to express the upper bound of time complexity.
  - After counting operations, express the complexity in terms of the most significant term.


Space Complexity

- Space complexity is concerned with how much memory (space) an algorithm uses as a function of the input size.
- This includes the space used by variables, data structures, function call stacks, and so on.

- Steps to analyze space complexity:
  - Identify the space used by input:
    - Space complexity typically depends on how much extra space is used relative to the input size. Space used by the input itself is generally not counted unless we modify it.
  - Account for all variables and data structures:
    - Consider any additional space used by arrays, hash maps, stacks, or other data structures within the function.
  - Consider recursion:
    - If the function is recursive, space complexity can be affected by the call stack. Each recursive call adds a new layer to the stack, and in some cases, this contributes to space complexity.
  - Simplify to Big-O notation:
    - Just like time complexity, space complexity is often simplified to Big-O notation.



Measuring Time and Space Complexity:
- Time Complexity: Focus on the loops, recursive calls, and nested operations. A good rule of thumb is:
  - Single loop: O(n)
  - Nested loops: O(n²), O(n³), etc.
  - Recursion depth: O(log n), O(n), depending on how the problem is divided.

- Space Complexity: Focus on extra space used, including:
  - Additional variables or data structures (arrays, dictionaries, etc.).
  - Space used by recursion (call stack depth).
  - Note that input data size is usually not counted unless we explicitly modify or store a large copy of the input.


In summary:
- Time complexity is measured by counting the number of operations relative to the input size.
- Space complexity is measured by considering how much extra memory the function uses.
'''


################### TIME #######################

# -------- Constant Time O(1) ---------- #
# Only one operation
# -------------------------------- #
def constant_time_example(arr):
    return arr[0]



# -------- Linear Time O(n) --------- #
# Iterate through all elements
# The function iterates over all n elements in the list arr, so the time complexity is O(n).
# ---------------------------------- #
def linear_time_example(arr):
    for element in arr:
        print(element)


# ---------- Quadratic Time O(n²) ----------- #
# Two nested loops
# The function has two nested loops, each of size n, resulting in O(n²) time complexity.
# ------------------------------------------ #
def quadratic_time_example(arr):
    for i in arr:
        for j in arr:
            print(i, j)



# ---------- Logarithmic Time O(log n) ----------#
# Halving the value each time.
# The number of times the loop runs is proportional to the logarithm of n.
# ------------------------------------------ #
def logarithmic_time_example(n):
    while n > 1:
        n = n // 2




# ---------- Linearithmic Time O(n log n) ------------- #
# Sorting takes O(n log n)
# Common algorithms like Merge Sort and Quick Sort have time complexity O(n log n) because they divide the problem in each recursive step and then combine the results.
# ------------------------------------------ #
def linearithmic_time_example(arr):
    arr.sort()



################### SPACE #######################

# -------- Constant Space O(1) ----------#
# This function uses a single variable (result) for storage, regardless of the input size, so the space complexity is O(1).
# ------------------------------------------ #
def constant_space_example(n):
    result = 0
    for i in range(n):
        result += i
    return result



# -------- Linear Space O(n) ----------#
# The function creates a new list result that grows with the size of the input arr, so the space complexity is O(n).
# ------------------------------------------ #
def linear_space_example(arr):
    result = []
    for element in arr:
        result.append(element)
    return result



# -------- Space Complexity for Recursion ----------#
# This recursive function has a space complexity of O(n) because there will be n calls on the call stack before it reaches the base case.
# ------------------------------------------ #
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)



################### MEASURING TIME #######################
import time

ex_arr = [1, 2, 3, 4, 5]

def find_time(example_function, arr):
  start_time = time.time()
  example_function(arr) # Call the example function
  end_time = time.time()
  return f"Execution time: {end_time - start_time} seconds"

print("constant_time_example", find_time(constant_time_example, ex_arr))
print("------------")
print("linear_time_example", find_time(linear_time_example, ex_arr))
print("------------")
print("quadratic_time_example", find_time(quadratic_time_example, ex_arr))
print("------------")
print("logarithmic_time_example", find_time(logarithmic_time_example, 5))
print("------------")
print("linearithmic_time_example", find_time(linearithmic_time_example, ex_arr))
print("------------")


################### MEASURING SPACE (simple) #######################
import sys


def find_space(arr):
  return f"Space used by arr: {sys.getsizeof(arr)} bytes"

print(find_space(ex_arr))
