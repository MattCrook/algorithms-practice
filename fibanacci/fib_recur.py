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
