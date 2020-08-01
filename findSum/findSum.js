// Given two integers a and b, which can be positive or negative,
// find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.



// 1) First create a function to find the range of the two numbers, then can pass that in to our findSum function.
function findRange(start, stop) {
  let range = [];
  for (let i = start; i <= stop; i++) {
    range.push(i);
  }
  return range;
}

const r = findRange(4, 20);

function findSum(range) {
  return range.reduce((a, b) => a + b);
}
console.log("{findSum}", findSum(r));

// OR
function getSum(a, b) {
  if (a === b) return a;
  let range = findRange(a, b);
  let sum = range.reduce((a, b) => a + b);
  return sum;
}

console.log("{getSum}", getSum(4, 20));




// Using Generator Function, to be Fancy
function* range(start, end) {
  yield start;
  if (start === end) return;
  yield* range(start + 1, end);
}
console.log("Generator", ...range(5, 10));
