def fib_recur(n):
    if n <= 1:
        return n;
    else:
        return (fib_recur(n-1) + fib_recur(n-2))

nterms = int(input("How many terms?"))
if nterms <= 0:
    print("Please input a positive integer.")
else:
    print("Fibanacci Sequence:")
    for i in range(nterms):
        print(fib_recur(i))


# Run main.py to run the terminal input


# Compute the first (n) Fibonacci numbers

a, b = 0, 1
n = 10
for i in range(n):
    print(b)
    a, b = b, a + b

# 1, 1, 2, 3, 5, 8...
