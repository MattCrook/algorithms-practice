const prevValues = [];

const square = (n) => {
  if (prevValues[n] !== null) {
    return prevValues;
  }
  let result = 0;
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      result += 1;
    }
  }
  prevValues[n] = result;
  return result;
};


// fib sequence is add two previous numbers to get next number in sequence. (n) represents number we want to get in the fib sequence.
const fib = (n, prevValues = []) => {
  let result;
  if (n <= 2) {
    return 1;
  } else {
    result = fib(n - 1, prevValues) + fib(n - 2, prevValues);
  }
  prevValues[n] = result;
  return result;
};

/*
Memoization is just the act of caching values so that they can be calculated quicker in the future. 
Memoization is really useful in all parts of programming, but where it is most useful is in dynamic programming.
In first example, we have an incredibly slow function (nested for loops), 
so we added a check to see if the previous values are already there (not equal to null), then
all we need to do is return that previous value of n. So saying, if we have already called this function with variable n,
just return the result...since we saved it below the loop.
In second example, using the fibanacci sequence to illistrate memoization.
Setting the prevValues array to hold numbers we have already calculated, and passing it down so the rest of function has
access to it. 
By passing in the number or index/ position of the fib sequence, we get the value in the fib sequence that is at that location. 
For example, fib(8) === 21; fib(9) === 34; fib(7) === 13; etc...
*/
