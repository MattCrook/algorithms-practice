###################################################
# Fibonacci Sequence
###################################################

#------------------------------------------#
# Iterative Approach
# Simple example of how to generate the Fibonacci sequence.
#
# Challenge: "get the first 10 numbers of the fibonacci sequence."
# - The function takes an integer numbers as input, which specifies how many Fibonacci numbers you want.
# - It starts with the first two numbers, 0 and 1, in the sequence.
# - Then, it uses a for loop to calculate each subsequent Fibonacci number and appends it to the fib_sequence list.
#-----------------------------------------#
def fibonacci_simple(numbers):
    # First two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    for i in range(2, numbers):
        next_fib_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib_number)

    return fib_sequence

print(fibonacci_simple(10)) # Get the first 10 Fibonacci numbers
print("------------------------")

#--------------------------#
# Another Simple Iterative Approach
# A second iterative approach (which is actually more efficient for larger values of n)
#--------------------------#
def fibonacci_simple_2(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence


print(fibonacci_simple_2(10)) # Get first 10 Fibonacci numbers
print("------------------------")


#--------------------------#
# Simple Recursive approach
# (which is more elegant but can be inefficient for large n due to recalculating the same values multiple times).
#--------------------------#
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


fibonacci_list = [fibonacci_recursive(i) for i in range(10)]  # Get the 10th Fibonacci number
print(fibonacci_list)


#######################################################################
# Using the Recursive approach, a simple fun little CLI tool...
# Allows you to input the number of Fib Sequence numbers you'd like.
######################################################################
def fib_recur(n):
    if n <= 1:
        return n;
    else:
        return (fib_recur(n-1) + fib_recur(n-2))

def fib_cli():
  nterms = int(input("How many terms?"))
  if nterms <= 0:
      print("Please input a positive integer.")
  else:
      print("Fibanacci Sequence:")
      for i in range(nterms):
          print(fib_recur(i))
      print("--------------------")

# Uncomment this to run.
# fib_cli()


#--------------------------#
# Another simple solution - using for loop (iterative approach)
# - starts with default 0,1
# - reassigns value of variables each iteration
# - "a" keeps track of current and becomes previous number, becomes "b", then "b" becomes the sum of both.
#--------------------------#

def fib(n):
  a, b = 0, 1
  for i in range(n):
      print(b)
      a, b = b, a + b

fib(10)
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
